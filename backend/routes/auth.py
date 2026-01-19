from flask import Blueprint,request,jsonify
from db import connect_db
import bcrypt
import sqlite3

auth = Blueprint('auth',__name__)

@auth.route('/register',methods=['POST'])
def register():
	data = request.json
	name = data['Name']
	email = data['Email Id']
	password = data['Password']
	hash_password = bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()
	

	try:
		with connect_db() as db:
			db.execute("INSERT INTO users(name,email,password) VALUES (?,?,?)",(name,email,hash_password))

			db.commit()
		return jsonify({'Status':'Registered'}),201
	except sqlite3.IntegrityError:
		return jsonify({'Status':'User already registered'}),409
	except Exception as e:
		return jsonify({'Status':'Error'}),500




@auth.route('/login',methods=['POST'])
def login():
	data = request.json
	email = data['Email Id']
	password = data['Password']
	try:
		with connect_db() as db:
			cursor = db.execute("SELECT id,password FROM users WHERE email=?",(email,))
			user = cursor.fetchone()
		if user and bcrypt.checkpw(password.encode(),user[1].encode()):
			return jsonify({'Status':'Login Sucess'}),200
		else:
			return jsonify({'Status':'Invalid Credentials'}),401
	except Exception as e:
		return jsonify({'Status':'Error'}),500


