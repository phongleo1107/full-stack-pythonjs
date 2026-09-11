# Pydantic Schemas - Describe API Data

from pydantic import BaseModel


class CourseCreate(BaseModel):
    name: str
    credits: int


class ClassCreate(BaseModel):
    course_id: int
    class_code: str
    teacher: str
    capacity: int
    tuition: int
    currency: str
    schedule: str  

class CourseRead(BaseModel):
    id: int
    name: str
    credits: int

class ClassRead(BaseModel):
    id: int
    course_id: int
    class_code: str
    teacher: str
    capacity: int
    registered: int
    tuition: int
    currency: str
    schedule: str