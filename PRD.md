# PRD — Course Registration App MVP

## 1. Mục tiêu

Xây dựng một web đăng ký môn học đơn giản để học và thực hành:

**React.js → HTTP/REST API → FastAPI → SQLAlchemy → PostgreSQL**

MVP **không có User/Authentication**.

Mỗi thao tác trên UI sẽ đi qua API và được lưu/truy vấn từ PostgreSQL.

### Mục tiêu chính

Hiểu được full-stack data flow:

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

MVP chỉ có **một trang chính**:

```text
Course Registration
│
├── Available Classes
│
├── Register
│
└── Registered Classes
```

Không có:

* Login
* User
* Authentication
* Authorization
* Admin
* Payment
* Notification
* AI
* WebSocket
* Redis
* Docker/Kubernetes
* Microservices

---

# 4. Core Features

## 4.1. Xem danh sách lớp học

React gọi:

```http
GET /classes
```

FastAPI lấy dữ liệu từ PostgreSQL và trả JSON.

Ví dụ:

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

React hiển thị:

| Chọn | Môn học              | TC | Lớp        | Giáo viên    | Sĩ số | Đã ĐK | Học phí | Lịch    |
| ---- | -------------------- | -: | ---------- | ------------ | ----: | ----: | ------: | ------- |
| □    | Advanced Programming |  3 | INT2204-01 | Nguyen Van A |    60 |    35 |    1.2M | Mon 1-3 |

---

# 5. Database

MVP chỉ cần **2 bảng**.

## Courses

```text
courses
├── id
├── name
└── credits
```

Ví dụ:

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

Một Course có thể có nhiều Class.

Ví dụ:

```text
Advanced Programming
│
├── INT2204-01
├── INT2204-02
└── INT2204-03
```

---

# 6. Registration trong MVP

Không cần `Users`.

Không cần bảng `Registrations` ở phiên bản đầu nếu mục tiêu chỉ là học CRUD + data flow.

Thay vào đó, frontend có thể giữ danh sách các lớp đã chọn trong state.

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

> Nếu muốn **registration phải tồn tại trong database** ngay từ MVP, có thể thêm bảng `Registrations` sau khi CRUD cơ bản chạy ổn. Không nên bắt đầu với nó nếu mục tiêu hiện tại là hiểu kiến trúc.

---

# 7. API

MVP chỉ cần các API sau.

## Courses

### Get courses

```http
GET /courses
```

Lấy danh sách môn học.

---

## Classes

### Get classes

```http
GET /classes
```

Lấy danh sách lớp học.

### Get one class

```http
GET /classes/{id}
```

Lấy thông tin một lớp.

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
1. Nhận class_id
2. Kiểm tra class tồn tại
3. Kiểm tra còn chỗ
4. Tăng registered
5. Commit database
6. Trả JSON
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

FastAPI giảm số lượng `registered`.

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

Không cần component architecture phức tạp.

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

React chịu trách nhiệm:

* Hiển thị dữ liệu
* Quản lý UI state
* Nhận input
* Gửi HTTP request
* Nhận JSON
* Cập nhật UI

---

# 10. Backend Structure

Có thể bắt đầu đơn giản:

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

Không cần architecture quá phức tạp ở MVP.

Mục tiêu là hiểu:

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

`Class` có:

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
JSON
        ↓
React
        ↓
Update UI
```

---

# 13. MVP Learning Goals

Sau khi hoàn thành MVP, cần hiểu được:

### React

* Component
* Props
* State
* Event handling
* `useEffect`
* Fetch API
* Render data từ API

### HTTP / REST

* GET
* POST
* DELETE
* Request body
* Response
* Status code
* JSON

### FastAPI

* Routes
* Path parameters
* Request body
* Pydantic schemas
* Response models
* Basic validation
* Error handling

### SQLAlchemy

* Model
* Column
* Foreign key
* Relationship
* Query
* Insert
* Update
* Delete
* Commit

### PostgreSQL

* Table
* Primary key
* Foreign key
* CRUD
* `SELECT`
* `INSERT`
* `UPDATE`
* `DELETE`
* Relationships

### Full-stack

Quan trọng nhất:

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

MVP được xem là hoàn thành khi có thể:

* [ ] Hiển thị classes từ PostgreSQL lên React.
* [ ] Tạo course/class trong database.
* [ ] React gọi được FastAPI.
* [ ] FastAPI query được PostgreSQL.
* [ ] Register một class.
* [ ] Unregister một class.
* [ ] `registered` được cập nhật trong database.
* [ ] React cập nhật UI sau mỗi request.
* [ ] Hiểu được dữ liệu đi qua từng layer.

---

# 15. Sau MVP

Chỉ sau khi MVP hoạt động ổn định mới mở rộng:

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

Authentication là **phase 2**, không phải một phần của MVP.
