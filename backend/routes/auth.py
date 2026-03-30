from flask import Blueprint, request, jsonify, session, current_app
import pymysql
from db import connect_db
import bcrypt
import re
from token_generater.token_gen import generate_password_reset_token
import jwt
from flask_mail import Message
from mail_server import mail
import os


auth = Blueprint('auth', __name__)

NAME_REGEX = r"[A-Za-z\s\'-]{2,20}$"
EMAIL_REGEX = r'^[\w.+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'


def _json_payload():
	data = request.get_json(silent=True)
	if not isinstance(data, dict):
		return None
	return data


def _required_text(data, field_name):
	value = data.get(field_name)
	if value is None:
		return None
	text = str(value).strip()
	return text if text else None


@auth.route('/register', methods=['POST'])
def register():
	data = _json_payload()
	if data is None:
		return jsonify({'Status': 'Invalid JSON body'}), 400

	name = _required_text(data, 'Name')
	email = _required_text(data, 'Email Id')
	password = _required_text(data, 'Password')

	if not name or not email or not password:
		return jsonify({'Status': 'Name, Email Id and Password are required'}), 400
	if len(password) < 6:
		return jsonify({'Status': 'Password must be at least 6 characters'}), 400
	if not re.fullmatch(NAME_REGEX, name):
		return jsonify({'Status': 'Invalid Name syntax'}), 400
	if not re.fullmatch(EMAIL_REGEX, email):
		return jsonify({'Status': 'Invalid email syntax'}), 400

	conn = connect_db()
	cursor = None
	try:
		hash_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute('USE Bhasabridge')
		cursor.execute(
			'INSERT INTO users(name,email,password) VALUES (%s,%s,%s)',
			(name, email, hash_password),
		)
		conn.commit()
		return jsonify({'Status': 'Registered'}), 201
	except pymysql.err.IntegrityError as e:
		conn.rollback()
		if e.args and e.args[0] == 1062:
			return jsonify({'Status': 'User already registered'}), 409
		return jsonify({'Status': 'Database error', 'error': str(e)}), 500
	finally:
		if cursor:
			cursor.close()
		conn.close()


@auth.route('/login', methods=['POST'])
def login():
	data = _json_payload()
	if data is None:
		return jsonify({'Status': 'Invalid JSON body'}), 400

	email = _required_text(data, 'Email Id')
	password = _required_text(data, 'Password')

	if not email or not password:
		return jsonify({'Status': 'Email Id and Password are required'}), 400
	if not re.fullmatch(EMAIL_REGEX, email):
		return jsonify({'Status': 'Invalid email syntax'}), 400

	conn = connect_db()
	cursor = None
	user = None
	try:
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute('USE Bhasabridge')
		cursor.execute('SELECT id,password,name FROM users WHERE email=%s', (email,))
		user = cursor.fetchone()
	except Exception:
		return jsonify({'Status': 'Error'}), 500
	finally:
		if cursor:
			cursor.close()
		conn.close()

	if user and bcrypt.checkpw(password.encode(), user['password'].encode()):
		session['user_id'] = user['id']
		session['user_name'] = user['name']
		return jsonify({'Status': 'Login Success', 'Username': user['name']}), 200
	return jsonify({'Status': 'Invalid Credentials'}), 401


@auth.route('/logout', methods=['POST'])
def logout():
	session.clear()
	return jsonify({'Status': 'Logged out'}), 200


@auth.route('/request_reset', methods=['POST'])
def request_reset():
	data = _json_payload()
	if data is None:
		return jsonify({'Status': 'Invalid JSON body'}), 400

	email = _required_text(data, 'Email Id')
	if not email:
		return jsonify({'Status': 'Email Id is required'}), 400
	if not re.fullmatch(EMAIL_REGEX, email):
		return jsonify({'Status': 'Invalid Email Syntax'}), 400

	conn = connect_db()
	cursor = None
	try:
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute('USE Bhasabridge')
		cursor.execute('SELECT id FROM users WHERE email=%s', (email,))
		user = cursor.fetchone()
	finally:
		if cursor:
			cursor.close()
		conn.close()

	if not user:
		return jsonify({'Status': 'No user with this email'}), 404

	try:
		user_id = user['id']
		token = generate_password_reset_token(user_id)
		msg = Message(
			subject='Password Reset Request',
			sender=os.getenv('MAIL_USERNAME'),
			recipients=[email],
		)
		msg.body = f"""Hello,

Your token to reset your password is:

{token}

It expires in 5 minutes. If you did not request a password reset, please ignore this email.
"""
		mail.send(msg)
		return jsonify({'Status': 'Reset password email sent'}), 200
	except Exception as e:
		return jsonify({'Status': 'Reset Link Generation Failed', 'error': str(e)}), 500


@auth.route('/reset_password', methods=['POST'])
def reset_password():
	data = _json_payload()
	if data is None:
		return jsonify({'Status': 'Invalid JSON body'}), 400

	token = _required_text(data, 'Token')
	new_password = _required_text(data, 'New Password')

	if not token or not new_password:
		return jsonify({'Status': 'Token and New Password are required'}), 400
	if len(new_password) < 6:
		return jsonify({'Status': 'Password too Short'}), 400

	try:
		payload = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
	except jwt.ExpiredSignatureError:
		return jsonify({'Status': 'Expired Token'}), 400
	except jwt.InvalidTokenError:
		return jsonify({'Status': 'Invalid Token'}), 400

	user_id = payload.get('user_id')
	if not user_id:
		return jsonify({'Status': 'Invalid Token'}), 400

	conn = connect_db()
	cursor = None
	try:
		hash_password = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt()).decode()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute('USE Bhasabridge')
		cursor.execute('UPDATE users SET password=%s WHERE id=%s', (hash_password, user_id))
		if cursor.rowcount == 0:
			conn.rollback()
			return jsonify({'Status': 'User not found'}), 404
		conn.commit()
		return jsonify({'Status': 'Password Reset Success'}), 200
	except Exception:
		conn.rollback()
		return jsonify({'Status': 'Password Reset Failed'}), 500
	finally:
		if cursor:
			cursor.close()
		conn.close()
