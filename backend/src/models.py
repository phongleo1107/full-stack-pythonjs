# Describe Databases Table

from sqlalchemy import String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

from app.core.config import config

engine = create_engine(config.db_url, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


class Courses(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)
    credits: Mapped[int] = mapped_column(Integer)


class Classes(Base):
    __tablename__ = "classes"

    id: Mapped[int] = mapped_column(primary_key=True)
    course_id: Mapped(int) = mapped_column(
        ForeignKey("courses.id")
    )

    class_code: Mapped[str] = mapped_column(String, unique=True)
    teacher: Mapped[str] = mapped_column(String)
    capacity: Mapped[int] = mapped_column(Integer)
    registered: Mapped[int] = mapped_column(Integer)
    tuition: Mapped[int] = mapped_column(Integer)
    currency: Mapped[str] = mapped_column(String)
    schedule: Mapped[str] = mapped_column(String)

