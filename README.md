# BhasaBridge - Language Learning Platform

A comprehensive language learning web application with separate frontend and backend architecture.

## 🌟 Features

- User authentication (Register/Login)
- Interactive lessons with multiple difficulty levels
- Practice exercises (Multiple choice, Fill in the blank, Translation)
- Progress tracking and statistics
- User dashboard with personalized learning paths

## 📁 Project Structure

```
bhasabridge/
├── frontend/          # React frontend application
├── backend/           # Flask backend API
├── database/          # Database schema and seed data
├── docs/              # Project documentation
├── .gitignore
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- **Frontend:** Node.js 16+ and npm
- **Backend:** Python 3.8+
- Git

### Installation

#### 1. Clone the repository

```bash
git clone <repository-url>
cd bhasabridge
```

#### 2. Frontend Setup

```bash
cd frontend
npm install
npm start
```

The frontend will run on `http://localhost:3000`

#### 3. Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

The backend will run on `http://localhost:5000`

## 📚 Documentation

- [API Documentation](docs/API_DOCUMENTATION.md)
- [User Flow](docs/USER_FLOW.md)
- [Database Schema](database/schema.sql)

## 🔧 Development

### Branch Strategy

- `main` - Production-ready code
- `frontend` - Frontend development branch
- `backend` - Backend development branch
- `feature/*` - Feature-specific branches

### Working with Branches

See the "Git Branch Management" section below for detailed instructions.

## 🗄️ Database

Initialize the database:

```bash
cd backend
python
>>> from config.database import init_db
>>> init_db()
```

## 🤝 Contributing

1. Create a feature branch from `frontend` or `backend`
2. Make your changes
3. Submit a pull request

## 📝 License

This project is open source and available under the MIT License.

