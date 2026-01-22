# BhasaBridge API Documentation

## Base URL

```
http://localhost:5000/api
```

## Authentication Endpoints

### 1. Register User

**Endpoint:** `POST /api/register`

**Description:** Register a new user account

**Request Body:**

```json
{
  "Name": "John Doe",
  "Email Id": "john@example.com",
  "Password": "securepassword123"
}
```

**Success Response (201):**

```json
{
  "Status": "Registered"
}
```

**Error Responses:**

- **400 Bad Request:** Missing required fields
- **409 Conflict:** User already registered
- **500 Internal Server Error:** Server error

---

### 2. Login User

**Endpoint:** `POST /api/login`

**Description:** Login an existing user

**Request Body:**

```json
{
  "Email Id": "john@example.com",
  "Password": "securepassword123"
}
```

**Success Response (200):**

```json
{
  "Status": "Login Success",
  "userId": 1
}
```

**Error Responses:**

- **400 Bad Request:** Missing required fields
- **401 Unauthorized:** Invalid credentials
- **500 Internal Server Error:** Server error

---

## Future Endpoints (To be implemented)

### Lessons Management

- `GET /api/lessons` - Get all lessons
- `GET /api/lessons/:id` - Get specific lesson
- `POST /api/lessons` - Create new lesson (Admin)
- `PUT /api/lessons/:id` - Update lesson (Admin)
- `DELETE /api/lessons/:id` - Delete lesson (Admin)

### Exercises

- `GET /api/lessons/:id/exercises` - Get exercises for a lesson
- `POST /api/exercises/submit` - Submit exercise answer
- `GET /api/exercises/:id` - Get specific exercise

### User Progress

- `GET /api/progress/:userId` - Get user progress
- `POST /api/progress` - Update user progress
- `GET /api/progress/:userId/stats` - Get user statistics

### Dashboard

- `GET /api/dashboard/:userId` - Get user dashboard data

---

## Error Codes

| Code | Description           |
| ---- | --------------------- |
| 200  | Success               |
| 201  | Created               |
| 400  | Bad Request           |
| 401  | Unauthorized          |
| 404  | Not Found             |
| 409  | Conflict              |
| 500  | Internal Server Error |

---

## Notes

- All endpoints require `Content-Type: application/json` header
- Future versions will include JWT authentication tokens
- CORS is enabled for frontend development
