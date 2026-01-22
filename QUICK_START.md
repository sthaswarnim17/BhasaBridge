# 🚀 Quick Start Guide

## For Frontend Developer (You)

### Initial Setup (One Time)

```bash
cd d:\WebDev\WEBProg\Project\bhasabridge\frontend
npm install
```

### Daily Work

```bash
# 1. Switch to frontend branch
git checkout frontend

# 2. Pull latest changes
git pull origin frontend

# 3. Start development server
cd frontend
npm start

# 4. Make your changes in frontend/ directory

# 5. Commit and push
git add .
git commit -m "Your descriptive message"
git push origin frontend
```

---

## For Backend Developer (Team Member)

### Initial Setup (One Time)

```bash
cd d:\WebDev\WEBProg\Project\bhasabridge\backend
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### Daily Work

```bash
# 1. Switch to backend branch
git checkout backend

# 2. Pull latest changes
git pull origin backend

# 3. Activate virtual environment
cd backend
venv\Scripts\activate  # Windows

# 4. Start development server
python app.py

# 5. Make your changes in backend/ directory

# 6. Commit and push
git add .
git commit -m "Your descriptive message"
git push origin backend
```

---

## File Locations Quick Reference

### Where to work:

**Frontend Developer:**

- React Components: `frontend/src/components/`
- Styles: `frontend/src/components/*/**.css`
- Main App: `frontend/src/App.js`
- Assets: `frontend/src/components/Auth/`

**Backend Developer:**

- API Routes: `backend/routes/`
- Controllers: `backend/controllers/`
- Models: `backend/models/`
- Database Config: `backend/config/`

---

## Running Both Servers

### Terminal 1 (Frontend):

```bash
cd frontend
npm start
```

Runs on: `http://localhost:3000`

### Terminal 2 (Backend):

```bash
cd backend
venv\Scripts\activate
python app.py
```

Runs on: `http://localhost:5000`

---

## Common Git Commands

```bash
# Check what branch you're on
git branch

# Switch branches
git checkout frontend
git checkout backend

# See what changed
git status
git diff

# Undo changes
git checkout -- filename

# Pull latest code
git pull origin frontend
```

---

## Project Structure at a Glance

```
bhasabridge/
├── frontend/          👈 Frontend developer works here
│   ├── src/
│   │   └── components/
│   └── package.json
│
├── backend/           👈 Backend developer works here
│   ├── routes/
│   ├── controllers/
│   ├── models/
│   └── requirements.txt
│
├── database/          👈 Shared database schemas
└── docs/              👈 Shared documentation
```

---

## Need More Details?

- **Git workflow**: See `GIT_BRANCH_MANAGEMENT.md`
- **Complete setup**: See `SETUP_COMPLETE.md`
- **API docs**: See `docs/API_DOCUMENTATION.md`
