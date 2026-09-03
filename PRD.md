# PRD — Web Đăng Ký Môn Học

## 1. Mục tiêu

Xây dựng một web đơn giản mô phỏng hệ thống đăng ký môn học để học cách các thành phần:

**React/JavaScript → FastAPI/Python → PostgreSQL/SQL**

giao tiếp và xử lý dữ liệu với nhau.

---

## 2. Tech Stack

* **Frontend:** React + JavaScript
* **Backend:** FastAPI + Python
* **Database:** PostgreSQL
* **ORM:** SQLAlchemy

---

## 3. Chức năng

### 3.1. Đăng nhập

Trang Login gồm:

* Họ tên
* Mật khẩu
* Nút Đăng nhập

Đăng nhập thành công → chuyển tới trang đăng ký môn học.

---

### 3.2. Trang đăng ký môn học

Hiển thị:

**Đăng ký học ngành X — Học kỳ X năm YYYY-YYYY**

#### Bảng 1 — Danh sách môn học

| Chọn | Môn học | TC | Điểm | Lớp MH | Tổng SV | Đã ĐK | Chuyên ngành | Giáo viên | Học phí | Lịch học |
| ---- | ------- | -: | ---: | ------ | ------: | ----: | ------------ | --------- | ------: | -------- |

Sinh viên có thể:

* Xem danh sách môn học.
* Chọn môn học.
* Đăng ký môn học.

---

#### Bảng 2 — Môn học đã đăng ký

| STT | Môn học | TC | Lớp MH | Giáo viên | Lịch học | Ngành 1 | Ngành 2 | Kiểu ĐK | Hủy |
| --- | ------- | -: | ------ | --------- | -------- | ------- | ------- | ------- | --- |

Sinh viên có thể:

* Xem các môn đã đăng ký.
* Chọn môn thuộc ngành 1 hoặc ngành 2.
* Hủy môn học.

---

### 3.3. Tổng kết

Cuối trang hiển thị:

* **Tổng số tín chỉ đã đăng ký:** X
* **Tổng số môn học đã đăng ký:** X
* **Xem và in**

---

### 3.4. Xem và in

Hiển thị danh sách môn học đã đăng ký dưới dạng bảng.

Cho phép sử dụng chức năng **Print của trình duyệt** để in.

**Không cần export Word ở phiên bản đầu.**

---

## 4. Database

Các bảng chính:

### Users

```text
id
full_name
password
```

### Courses

```text
id
name
credits
major
```

### Classes

```text
id
course_id
class_code
teacher
capacity
registered
tuition
schedule
```

### Registrations

```text
id
user_id
class_id
major_1
major_2
registration_type
```

Quan hệ:

```text
User
  │
  └── Registrations
          │
          └── Class
                │
                └── Course
```

---

## 5. API cơ bản

### Authentication

```http
POST /login
```

### Courses / Classes

```http
GET /courses
GET /classes
```

### Registration

```http
GET    /registrations
POST   /registrations
DELETE /registrations/{id}
```

---

## 6. Luồng hoạt động

```text
React
  │
  │ HTTP Request
  ▼
FastAPI
  │
  │ SQL / SQLAlchemy
  ▼
PostgreSQL
  │
  │ Data
  ▼
FastAPI
  │
  │ JSON
  ▼
React
  │
  ▼
UI
```

Ví dụ khi sinh viên đăng ký:

```text
Click "Đăng ký"
      ↓
React gửi POST request
      ↓
FastAPI nhận request
      ↓
FastAPI validate dữ liệu
      ↓
SQLAlchemy tạo Registration
      ↓
PostgreSQL lưu dữ liệu
      ↓
FastAPI trả JSON
      ↓
React cập nhật bảng
```

## 7. Mục tiêu học tập

Sau project, có thể hiểu được:

1. **JavaScript/React** — UI và gọi API.
2. **HTTP/REST API** — frontend giao tiếp với backend.
3. **Python/FastAPI** — xử lý request và business logic.
4. **Pydantic** — validate dữ liệu.
5. **SQLAlchemy** — Python làm việc với database.
6. **SQL/PostgreSQL** — lưu trữ và truy vấn dữ liệu.
7. **Database relationships** — hiểu `User → Registration → Class → Course`.
8. **Full-stack data flow** — dữ liệu đi từ UI → API → Python → SQL → ngược lại.

## 8. Không làm trong MVP

* Admin
* AI/LLM
* Thanh toán
* Email
* Notification
* Docker/Kubernetes
* Microservices
* Redis
* WebSocket
* Phân quyền phức tạp
* Export Word
* Tối ưu lịch học
