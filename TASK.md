# TASK — Course Registration App MVP

## Project

**Goal:** Build a small full-stack course registration app to understand:

```text
React.js
    ↓ HTTP / JSON
FastAPI
    ↓ SQLAlchemy
PostgreSQL
    ↓
FastAPI
    ↓ JSON
React.js
```

The MVP intentionally has **no authentication, users, authorization, admin, or other production features**.

---

# 0. Current Progress

## Setup — DONE

### Frontend

- [x] Create Vite app
- [x] React
- [x] JavaScript
- [x] ESLint

Current location:

```text
frontend/app/
```

The repository currently contains the standard Vite React structure with `src/`, `package.json`, `eslint.config.js`, `vite.config.js`, etc.

### Backend

- [x] Initialize Python project with `uv`
- [x] FastAPI
- [x] Pydantic / FastAPI validation
- [x] PostgreSQL installed / available

Current backend structure:

```text
backend/
├── src/
│   └── backend/
│       └── __init__.py
├── pyproject.toml
├── uv.lock
└── ...
```

### Testing

- [ ] No testing setup yet

Do **not** add testing infrastructure before the first working API flow. Testing will be added after the basic CRUD/data flow works.

---

# 1. MVP Scope

## Main goal

Implement:

```text
Input
  ↓
React
  ↓
HTTP Request
  ↓
FastAPI
  ↓
SQLAlchemy
  ↓
PostgreSQL
  ↓
FastAPI
  ↓
JSON Response
  ↓
React
  ↓
Output
```

## Not in MVP

- [ ] Authentication
- [ ] Login
- [ ] Users
- [ ] Authorization
- [ ] Admin
- [ ] JWT
- [ ] Payment
- [ ] Email
- [ ] Notifications
- [ ] AI/LLM
- [ ] Redis
- [ ] WebSocket
- [ ] Docker/Kubernetes
- [ ] Microservices
- [ ] Complex scheduling optimization
- [ ] Word export

Authentication can be added in a later phase.

---

# 2. Recommended Project Structure

Start simple:

```text
full-stack-pythonjs/
│
├── frontend/
│   └── app/
│       ├── src/
│       │   ├── components/
│       │   ├── services/
│       │   ├── App.jsx
│       │   └── main.jsx
│       ├── package.json
│       └── ...
│
├── backend/
│   ├── src/
│   │   └── backend/
│   │       ├── __init__.py
│   │       ├── main.py
│   │       ├── database.py
│   │       ├── models.py
│   │       ├── schemas.py
│   │       └── routes/
│   │           ├── courses.py
│   │           ├── classes.py
│   │           └── registrations.py
│   │
│   ├── pyproject.toml
│   └── uv.lock
│
├── PRD.md
├── TASK.md
└── README.md
```

## Database folder?

**Do not create a separate top-level `database/` folder yet.**

PostgreSQL is the database service. The code that connects to it belongs to the backend.

For the MVP:

```text
backend/src/backend/
├── database.py   # database engine + session
├── models.py     # SQLAlchemy models
└── schemas.py    # Pydantic schemas
```

Later, if database migrations/seeding become more substantial, add something such as:

```text
backend/
└── alembic/
```

or a dedicated SQL/migration directory.

Do **not** store PostgreSQL's actual data files inside the repository.

---

# 3. Database Design

MVP uses two main tables.

## Courses

```text
courses
├── id          INTEGER PK
├── name        VARCHAR UNIQUE
└── credits     INTEGER
```

## Classes

```text
classes
├── id           INTEGER PK
├── course_id    INTEGER FK → courses.id
├── class_code   VARCHAR UNIQUE
├── teacher      VARCHAR
├── capacity     INTEGER
├── registered   INTEGER
├── tuition      INTEGER
└── schedule     VARCHAR
```

Relationship:

```text
Course 1 ───────< N Class
```

Important:

- `credits` should be an integer, not a string.
- `tuition` should be an integer, not a string.
- `course_id` is a foreign key referencing `courses.id`.
- `registered` represents the current number of registered students in the MVP.

---

# 4. Backend Setup

## 4.1 Database connection

- [ ] Install SQLAlchemy
- [ ] Install PostgreSQL driver
- [ ] Create `database.py`
- [ ] Configure PostgreSQL connection
- [ ] Create SQLAlchemy engine
- [ ] Create session factory
- [ ] Create database dependency for FastAPI

Target concept:

```text
FastAPI
   ↓
SQLAlchemy Session
   ↓
PostgreSQL
```

---

# 5. SQLAlchemy Models

## Course model

- [ ] Create `Course` model
- [ ] Add `id`
- [ ] Add `name`
- [ ] Add `credits`

## Class model

- [ ] Create `Class` model
- [ ] Add `id`
- [ ] Add `course_id`
- [ ] Add `class_code`
- [ ] Add `teacher`
- [ ] Add `capacity`
- [ ] Add `registered`
- [ ] Add `tuition`
- [ ] Add `schedule`

## Relationship

- [ ] Define `Course → Classes`
- [ ] Define foreign key `classes.course_id → courses.id`

---

# 6. Pydantic Schemas

Create schemas for API input/output.

## Course

- [ ] CourseCreate
- [ ] CourseResponse

## Class

- [ ] ClassCreate
- [ ] ClassResponse

Keep Pydantic schemas separate from SQLAlchemy models.

Concept:

```text
Request JSON
    ↓
Pydantic Schema
    ↓
SQLAlchemy Model
    ↓
PostgreSQL
```

---

# 7. Courses API

Implement basic CRUD.

## Create

```http
POST /courses
```

Input:

```json
{
  "name": "Advanced Programming",
  "credits": 3
}
```

- [ ] Validate input
- [ ] Create Course
- [ ] Save to PostgreSQL
- [ ] Return JSON

## Read

```http
GET /courses
```

- [ ] Query PostgreSQL
- [ ] Return course list

## Update

```http
PUT /courses/{id}
```

- [ ] Find course
- [ ] Validate input
- [ ] Update course
- [ ] Commit
- [ ] Return updated course

## Delete

```http
DELETE /courses/{id}
```

- [ ] Find course
- [ ] Delete course
- [ ] Commit
- [ ] Return success response

---

# 8. Classes API

Implement basic CRUD.

## Create

```http
POST /classes
```

Example:

```json
{
  "course_id": 1,
  "class_code": "INT2204-01",
  "teacher": "Nguyen Van A",
  "capacity": 60,
  "registered": 0,
  "tuition": 1200000,
  "schedule": "Mon 1-3"
}
```

- [ ] Validate `course_id`
- [ ] Create Class
- [ ] Save to PostgreSQL
- [ ] Return JSON

## Read

```http
GET /classes
```

- [ ] Query classes
- [ ] Include course information where useful
- [ ] Return JSON

## Read one

```http
GET /classes/{id}
```

- [ ] Find class
- [ ] Return JSON
- [ ] Return appropriate error if not found

## Update

```http
PUT /classes/{id}
```

- [ ] Update class
- [ ] Commit
- [ ] Return updated class

## Delete

```http
DELETE /classes/{id}
```

- [ ] Delete class
- [ ] Commit
- [ ] Return success response

---

# 9. Registration MVP

There is **no User table** and **no persistent Registration table** yet.

Registration is represented by the selected classes in the frontend.

## Register

```http
POST /registrations
```

Input:

```json
{
  "class_id": 1
}
```

Backend:

- [ ] Validate `class_id`
- [ ] Check class exists
- [ ] Check capacity
- [ ] Increase `registered`
- [ ] Commit transaction
- [ ] Return updated data

## Unregister

```http
DELETE /registrations/{class_id}
```

Backend:

- [ ] Check class exists
- [ ] Prevent `registered` from becoming negative
- [ ] Decrease `registered`
- [ ] Commit
- [ ] Return updated data

---

# 10. Frontend

## Main page

Create one simple page:

```text
Course Registration

Available Classes
─────────────────────────────

Course | Class | Teacher | Capacity | Registered | Action

                         [Register]


Registered Classes
─────────────────────────────

Course | Class | Teacher | Credits | Action

                         [Remove]


Total Credits: X
```

---

# 11. React Components

Keep the component structure simple.

- [ ] `ClassList`
- [ ] `ClassRow`
- [ ] `RegistrationList`
- [ ] `RegistrationRow`
- [ ] `Summary`

Do not introduce Redux or another state-management library for the MVP.

Use React state first.

---

# 12. Frontend API Layer

Create a small service layer:

```text
frontend/app/src/
└── services/
    └── api.js
```

Implement functions such as:

```javascript
getCourses()
getClasses()
createCourse()
createClass()
registerClass()
unregisterClass()
```

The components should call these functions instead of putting every `fetch()` directly inside the UI.

---

# 13. Connect Frontend → Backend

## First integration milestone

Get this working before building the whole UI:

```text
React
  ↓
GET /classes
  ↓
FastAPI
  ↓
PostgreSQL
  ↓
JSON
  ↓
React
```

- [ ] Start PostgreSQL
- [ ] Start FastAPI
- [ ] Verify API through `/docs`
- [ ] Create sample course/class data
- [ ] Call `/classes` from React
- [ ] Render returned data

This is the **first major milestone**.

---

# 14. CORS

Because frontend and backend run on different development origins:

- [ ] Configure FastAPI CORS
- [ ] Allow local React development origin
- [ ] Verify browser request succeeds

Do not use `allow_origins=["*"]` as the final production configuration.

---

# 15. Testing

## Current status

**No testing setup yet.**

That is fine at this stage.

Do not spend time setting up a large testing architecture before the first working API flow.

## After CRUD works

### Backend

Use:

```text
pytest
```

Test:

- [ ] `GET /courses`
- [ ] `POST /courses`
- [ ] `GET /classes`
- [ ] `POST /classes`
- [ ] Invalid `course_id`
- [ ] Non-existent class
- [ ] Capacity validation
- [ ] Registration
- [ ] Unregistration

### Frontend

Later add:

```text
Vitest
```

Test:

- [ ] Components render
- [ ] Class list displays API data
- [ ] Register button triggers expected action
- [ ] Remove button triggers expected action

### Integration / E2E

Not required for the first MVP.

Consider Playwright only after the basic application and unit/API tests work.

---

# 16. Error Handling

Implement basic API errors.

Examples:

```text
404
Class not found
```

```text
400
Class is already full
```

```text
422
Invalid request data
```

- [ ] Handle backend errors
- [ ] Display useful error messages in React
- [ ] Do not expose database internals to the frontend

---

# 17. MVP Definition of Done

The MVP is complete when this works end-to-end:

```text
Create Course
      ↓
PostgreSQL
      ↓
Create Class
      ↓
PostgreSQL
      ↓
React requests Classes
      ↓
FastAPI
      ↓
SQLAlchemy
      ↓
PostgreSQL
      ↓
JSON
      ↓
React table
      ↓
Register
      ↓
FastAPI
      ↓
PostgreSQL
      ↓
Updated registered count
      ↓
React updates UI
```

Checklist:

- [ ] PostgreSQL connected
- [ ] SQLAlchemy connected
- [ ] Course model works
- [ ] Class model works
- [ ] Course → Class relationship works
- [ ] Course CRUD works
- [ ] Class CRUD works
- [ ] `GET /classes` works
- [ ] React can call FastAPI
- [ ] Classes render in React
- [ ] Register works
- [ ] Unregister works
- [ ] Basic error handling works
- [ ] Basic backend tests added

---

# 18. Phase 2 — After MVP

Only after the MVP is stable:

## Authentication

- [ ] Users table
- [ ] Password hashing
- [ ] Login
- [ ] JWT/session
- [ ] Protected routes

## Persistent registrations

Add:

```text
registrations
├── id
├── user_id
└── class_id
```

Then change:

```text
User
  ↓
Registration
  ↓
Class
  ↓
Course
```

## Testing expansion

- [ ] More API tests
- [ ] Frontend component tests
- [ ] Integration tests
- [ ] E2E tests

## Deployment

- [ ] Environment variables
- [ ] Production PostgreSQL
- [ ] Backend deployment
- [ ] Frontend deployment

---

# 19. Priority Order

Work in this order:

```text
1. Database connection
        ↓
2. SQLAlchemy models
        ↓
3. Pydantic schemas
        ↓
4. GET /courses + GET /classes
        ↓
5. React fetches API
        ↓
6. Display data
        ↓
7. POST /courses + POST /classes
        ↓
8. PUT /courses + PUT /classes
        ↓
9. DELETE /courses + DELETE /classes
        ↓
10. Registration
        ↓
11. Error handling
        ↓
12. Testing
        ↓
13. MVP complete
```

Do not jump to authentication before this flow works.

---

# 20. Learning Principle

The purpose of this project is not to build a production-grade registration system.

The purpose is to understand:

```text
Frontend
    ↓
HTTP
    ↓
API
    ↓
Validation
    ↓
ORM
    ↓
SQL
    ↓
Database
```

Every major feature should make it clearer **where the data is coming from, where it goes, and which layer is responsible for processing it.**
