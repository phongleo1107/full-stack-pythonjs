# PRD — Course Registration App MVP

## 1. Objective

Build a simple course registration web application to learn and practice:

**React.js → HTTP/REST API → FastAPI → SQLAlchemy → PostgreSQL**

The MVP **does not include Users or Authentication**.

Every UI action goes through the API and reads from or writes to PostgreSQL.

### Main Goal

Understand the full-stack data flow:

```text
React
  ↓ HTTP Request
FastAPI
  ↓ SQLAlchemy
PostgreSQL
  ↓ Data
FastAPI
  ↓ JSON Response
React
  ↓
UI
```

---

# 2. Tech Stack

### Frontend

* React.js
* JavaScript
* Fetch API

### Backend

* Python
* FastAPI
* Pydantic
* SQLAlchemy

### Database

* PostgreSQL

---

# 3. MVP Scope

The MVP has **one main page**:

```text
Course Registration
│
├── Available Classes
│
├── Register
│
└── Registered Classes
```

Not included:

* Login
* User
* Authentication
* Authorization
* Admin
* Payment
* Notifications
* AI
* WebSocket
* Redis
* Docker/Kubernetes
* Microservices

---

# 4. Core Features

## 4.1. View Available Classes

React calls:

```http
GET /classes
```

FastAPI retrieves data from PostgreSQL and returns JSON.

Example:

```json
[
  {
    "id": 1,
    "course_name": "Advanced Programming",
    "credits": 3,
    "class_code": "INT2204-01",
    "teacher": "Nguyen Van A",
    "capacity": 60,
    "registered": 35,
    "tuition": 1200000,
    "schedule": "Mon 1-3"
  }
]
```

React displays:

| Select | Course               | Credits | Class      | Teacher      | Capacity | Registered | Tuition | Schedule |
| ------ | -------------------- | ------: | ---------- | ------------ | -------: | ---------: | ------: | -------- |
| □      | Advanced Programming |       3 | INT2204-01 | Nguyen Van A |       60 |         35 |    1.2M | Mon 1-3  |

---

# 5. Database

The MVP only needs **2 tables**.

## Courses

```text
courses
├── id
├── name
└── credits
```

Example:

```text
1 | Advanced Programming | 3
2 | Discrete Mathematics | 3
3 | Probability & Statistics | 3
```

## Classes

```text
classes
├── id
├── course_id
├── class_code
├── teacher
├── capacity
├── registered
├── tuition
└── schedule
```

Relationship:

```text
Course
  │
  └──< Classes
```

One Course can have multiple Classes.

Example:

```text
Advanced Programming
│
├── INT2204-01
├── INT2204-02
└── INT2204-03
```

---

# 6. Registration in the MVP

No `Users` table is required.

No `Registrations` table is required in the first version if the goal is to learn CRUD and data flow.

Instead, the frontend can keep the list of selected classes in React state.

```text
React State

registeredClasses
│
├── Class 1
├── Class 2
└── Class 3
```

Flow:

```text
User clicks "Register"
        ↓
React
        ↓
POST /registrations
        ↓
FastAPI
        ↓
Update registered count
        ↓
PostgreSQL
        ↓
JSON response
        ↓
React
        ↓
Update UI
```

> If registration needs to be persisted in the database during the MVP, a `Registrations` table can be added after the basic CRUD flow is working. It should not be introduced at the beginning if the current goal is to understand the architecture.

---

# 7. API

The MVP only needs the following APIs.

## Courses

### Get Courses

```http
GET /courses
```

Returns a list of courses.

---

## Classes

### Get Classes

```http
GET /classes
```

Returns a list of classes.

### Get One Class

```http
GET /classes/{id}
```

Returns information about a specific class.

---

## Registration

### Register

```http
POST /registrations
```

Request:

```json
{
  "class_id": 1
}
```

FastAPI:

```text
1. Receive class_id
2. Check whether the class exists
3. Check whether there is available capacity
4. Increase registered count
5. Commit to the database
6. Return JSON
```

Response:

```json
{
  "message": "Registration successful",
  "class_id": 1,
  "registered": 36
}
```

### Unregister

```http
DELETE /registrations/{class_id}
```

FastAPI decreases the `registered` count.

---

# 8. Frontend

## Main Page

```text
Course Registration
────────────────────────────────────────

Available Classes

┌────┬──────────────────────┬────┬───────┐
│    │ Course               │ TC │ Class │
├────┼──────────────────────┼────┼───────┤
│ □  │ Advanced Programming │ 3  │ ...   │
│ □  │ Discrete Mathematics │ 3  │ ...   │
└────┴──────────────────────┴────┴───────┘

              [ Register ]

────────────────────────────────────────

Registered Classes

┌──────────────────────┬────┬───────┐
│ Course               │ TC │ Action│
├──────────────────────┼────┼───────┤
│ Advanced Programming │ 3  │ Remove│
└──────────────────────┴────┴───────┘

Total Credits: 3
```

---

# 9. React Components

No complex component architecture is needed.

```text
App
│
├── ClassList
│   └── ClassRow
│
├── RegistrationList
│   └── RegistrationRow
│
└── Summary
```

React is responsible for:

* Displaying data
* Managing UI state
* Receiving user input
* Sending HTTP requests
* Receiving JSON
* Updating the UI

---

# 10. Backend Structure

Start simple:

```text
backend/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
└── routes/
    ├── courses.py
    ├── classes.py
    └── registrations.py
```

No complex architecture is needed for the MVP.

The goal is to understand:

```text
Route
  ↓
Pydantic Schema
  ↓
SQLAlchemy Model
  ↓
PostgreSQL
```

---

# 11. SQLAlchemy Models

Conceptual structure:

```text
Course
  │
  │ 1
  │
  │
  │ *
Class
```

`Class` has:

```text
course_id → courses.id
```

SQLAlchemy relationship:

```python
Course
    ↓
classes

Class
    ↓
course
```

---

# 12. Data Flow Examples

## GET Classes

```text
User opens website
        ↓
React
        ↓
GET /classes
        ↓
FastAPI
        ↓
SQLAlchemy
        ↓
PostgreSQL
        ↓
SELECT ...
        ↓
FastAPI
        ↓
JSON
        ↓
React
        ↓
Render table
```

## Register Class

```text
Click "Register"
        ↓
React
        ↓
POST /registrations
        ↓
FastAPI
        ↓
Validate class_id
        ↓
SQLAlchemy
        ↓
UPDATE classes
SET registered = registered + 1
        ↓
PostgreSQL
        ↓
FastAPI
        ↓
JSON
        ↓
React
        ↓
Update UI
```

## Unregister Class

```text
Click "Remove"
        ↓
React
        ↓
DELETE /registrations/{class_id}
        ↓
FastAPI
        ↓
SQLAlchemy
        ↓
UPDATE classes
SET registered = registered - 1
        ↓
PostgreSQL
        ↓
FastAPI
        ↓
JSON
        ↓
React
        ↓
Update UI
```

---

# 13. MVP Learning Goals

After completing the MVP, you should understand:

### React

* Components
* Props
* State
* Event handling
* `useEffect`
* Fetch API
* Rendering data from an API

### HTTP / REST

* GET
* POST
* DELETE
* Request body
* Response
* Status codes
* JSON

### FastAPI

* Routes
* Path parameters
* Request bodies
* Pydantic schemas
* Response models
* Basic validation
* Error handling

### SQLAlchemy

* Models
* Columns
* Foreign keys
* Relationships
* Queries
* Insert
* Update
* Delete
* Commit

### PostgreSQL

* Tables
* Primary keys
* Foreign keys
* CRUD
* `SELECT`
* `INSERT`
* `UPDATE`
* `DELETE`
* Relationships

### Full-Stack

Most importantly:

```text
Input
  ↓
React
  ↓
HTTP
  ↓
FastAPI
  ↓
Pydantic
  ↓
SQLAlchemy
  ↓
PostgreSQL
  ↓
SQLAlchemy
  ↓
FastAPI
  ↓
JSON
  ↓
React
  ↓
Output
```

---

# 14. Definition of Done

The MVP is considered complete when you can:

* [ ] Display classes from PostgreSQL in React.
* [ ] Create courses/classes in the database.
* [ ] React can communicate with FastAPI.
* [ ] FastAPI can query PostgreSQL.
* [ ] Register for a class.
* [ ] Unregister from a class.
* [ ] Update `registered` in the database.
* [ ] Update the React UI after each request.
* [ ] Understand how data flows through each layer.

---

# 15. After the MVP

Only expand the project after the MVP is working reliably:

```text
MVP
 │
 ├── Authentication
 │
 ├── Users
 │
 ├── Registrations table
 │
 ├── JWT
 │
 ├── Authorization
 │
 ├── Better validation
 │
 ├── Unit testing
 │
 └── Deployment
```

Authentication is **Phase 2**, not part of the MVP.