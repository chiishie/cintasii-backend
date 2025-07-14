# app/schemas.py
from pydantic import BaseModel
from typing import List, Optional

# --- Lesson Schemas ---
class LessonBase(BaseModel):
    title: str
    content_url: Optional[str] = None

class Lesson(LessonBase):
    id: int

    class Config:
        from_attributes = True

# --- Module Schemas ---
class ModuleBase(BaseModel):
    title: str

class Module(ModuleBase):
    id: int
    lessons: List[Lesson] = []

    class Config:
        from_attributes = True

# --- Course Schemas ---
class CourseBase(BaseModel):
    title: str
    description: Optional[str] = None

class Course(CourseBase):
    id: int

    class Config:
        from_attributes = True

class CourseDetail(Course):
    modules: List[Module] = []