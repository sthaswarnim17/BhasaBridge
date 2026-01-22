# Git Branch Management Guide for BhasaBridge

## 📋 Overview

This guide will help you and your team member work on separate branches and merge changes effectively.

## 🌳 Branch Structure

```
main (production)
├── frontend (your branch)
│   └── feature/frontend-* (feature branches)
└── backend (team member's branch)
    └── feature/backend-* (feature branches)
```

## 🚀 Initial Setup

### Step 1: Commit Current Changes to Main

```bash
# Make sure you're in the project root
cd d:\WebDev\WEBProg\Project\bhasabridge

# Add all new files
git add .

# Commit the restructured project
git commit -m "Restructure project with separate frontend and backend directories"

# Push to main branch (if remote exists)
git push origin main
```

### Step 2: Create Frontend Branch (For You)

```bash
# Create and switch to frontend branch
git checkout -b frontend

# Push frontend branch to remote
git push -u origin frontend
```

### Step 3: Create Backend Branch (For Your Team Member)

```bash
# Switch back to main
git checkout main

# Create and switch to backend branch
git checkout -b backend

# Push backend branch to remote
git push -u origin backend

# Switch back to frontend for your work
git checkout frontend
```

## 💻 Daily Workflow

### For Frontend Developer (You)

```bash
# Start your day - make sure you're on frontend branch
git checkout frontend

# Pull latest changes from remote
git pull origin frontend

# Create a feature branch for specific feature (optional but recommended)
git checkout -b feature/frontend-dashboard

# Make your changes to frontend files
# ... work on frontend/ directory ...

# Stage and commit your changes
git add frontend/
git commit -m "Add dashboard component with user stats"

# Push to your branch
git push origin frontend
# or if on feature branch:
git push origin feature/frontend-dashboard

# Merge feature back to frontend branch
git checkout frontend
git merge feature/frontend-dashboard
git push origin frontend
```

### For Backend Developer (Team Member)

```bash
# Start day on backend branch
git checkout backend

# Pull latest changes
git pull origin backend

# Create feature branch (optional)
git checkout -b feature/backend-lessons-api

# Make changes to backend files
# ... work on backend/ directory ...

# Commit and push
git add backend/
git commit -m "Add lessons API endpoints"
git push origin backend
```

## 🔄 Merging Changes

### Merging Backend into Main

When backend features are ready for production:

```bash
# Switch to main branch
git checkout main

# Pull latest main
git pull origin main

# Merge backend branch
git merge backend

# Resolve any conflicts if they arise
# ... fix conflicts ...
git add .
git commit -m "Merge backend features into main"

# Push to main
git push origin main
```

### Merging Frontend into Main

When your frontend features are ready:

```bash
# Switch to main branch
git checkout main

# Pull latest main
git pull origin main

# Merge frontend branch
git merge frontend

# Resolve conflicts if any
git push origin main
```

### Syncing Your Branch with Main

To get latest changes from main into your branch:

```bash
# On your frontend branch
git checkout frontend

# Merge main into frontend
git merge main

# Resolve conflicts if any
git push origin frontend
```

## 🔧 Handling Conflicts

When merge conflicts occur:

1. Git will mark conflicted files
2. Open conflicted files and look for conflict markers:

```
<<<<<<< HEAD
Your changes
=======
Their changes
>>>>>>> backend
```

3. Manually resolve conflicts by editing the file
4. Remove conflict markers
5. Stage resolved files:

```bash
git add <resolved-file>
```

6. Complete the merge:

```bash
git commit -m "Resolve merge conflicts between frontend and backend"
```

## 📝 Best Practices

### 1. Commit Often, Push Daily

```bash
# Small, frequent commits are better
git commit -m "Add login form validation"
git commit -m "Style login button"
git commit -m "Add error handling to auth"
```

### 2. Write Clear Commit Messages

```bash
# Good commit messages
git commit -m "Add user authentication with JWT tokens"
git commit -m "Fix: Dashboard not loading user progress"
git commit -m "Refactor: Extract auth logic into separate service"

# Bad commit messages
git commit -m "updates"
git commit -m "fix"
git commit -m "changes"
```

### 3. Pull Before Push

```bash
# Always pull before pushing to avoid conflicts
git pull origin frontend
git push origin frontend
```

### 4. Keep Branches Updated

```bash
# Weekly: sync your branch with main
git checkout frontend
git merge main
git push origin frontend
```

### 5. Use Feature Branches for Big Features

```bash
# For large features, create a sub-branch
git checkout frontend
git checkout -b feature/frontend-lesson-player
# ... work on feature ...
git checkout frontend
git merge feature/frontend-lesson-player
```

## 🎯 Common Commands Cheatsheet

```bash
# Check current branch
git branch

# Check status
git status

# See commit history
git log --oneline

# Discard changes in a file
git checkout -- <file>

# Undo last commit (keep changes)
git reset HEAD~1

# Undo last commit (discard changes)
git reset --hard HEAD~1

# See differences
git diff

# See differences between branches
git diff frontend backend

# List all branches
git branch -a

# Delete local branch
git branch -d feature/old-feature

# Delete remote branch
git push origin --delete feature/old-feature
```

## 🚨 Troubleshooting

### "Your branch is behind"

```bash
git pull origin frontend
```

### "Your branch is ahead"

```bash
git push origin frontend
```

### "merge conflict"

```bash
# 1. Open conflicted files
# 2. Resolve conflicts manually
# 3. Stage files
git add .
# 4. Commit
git commit -m "Resolve merge conflicts"
```

### "I committed to wrong branch"

```bash
# If you haven't pushed yet
git reset HEAD~1  # Undo commit
git stash        # Save changes
git checkout correct-branch
git stash pop    # Apply changes
git add .
git commit -m "Your message"
```

## 🤝 Collaboration Workflow

### Sprint Planning

1. Decide what features frontend and backend will work on
2. Ensure features don't conflict
3. Agree on API contracts/interfaces

### Daily Sync

1. Both developers push their changes daily
2. Quick standup to discuss progress
3. Communicate any API or structure changes

### Weekly Integration

1. Merge both branches into main
2. Test integration
3. Fix any integration issues
4. Tag release if needed

```bash
# Create a release tag
git checkout main
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
```

## 📞 Getting Help

If you're stuck:

1. Check `git status` to see current state
2. Check `git log` to see recent commits
3. Use `git reflog` to see all actions (can help undo mistakes)
4. Ask team member for help
5. Google the error message

## 🎉 Quick Start Commands

```bash
# FRONTEND DEVELOPER (YOU) - Daily Routine
git checkout frontend
git pull origin frontend
# ... do your work in frontend/ directory ...
git add frontend/
git commit -m "Descriptive message"
git push origin frontend

# BACKEND DEVELOPER - Daily Routine
git checkout backend
git pull origin backend
# ... do your work in backend/ directory ...
git add backend/
git commit -m "Descriptive message"
git push origin backend

# WEEKLY INTEGRATION - Either Developer
git checkout main
git merge frontend
git merge backend
# ... test everything works ...
git push origin main
```

---

Remember: **Communication is key!** Always let your team member know about:

- Breaking changes
- API modifications
- Directory structure changes
- Database schema updates
