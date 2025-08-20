# app/models.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class LearningTopic(Base):
    """Represents a high-level learning goal, e.g., 'Python for Data Science'."""
    __tablename__ = "learning_topics"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    # This relationship links a topic to its many modules.
    modules = relationship("LearningModule", back_populates="topic", cascade="all, delete-orphan")

class LearningModule(Base):
    """Represents a logical section of a topic, e.g., 'Week 1: Python Basics'."""
    __tablename__ = "learning_modules"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    module_order = Column(Integer)
    topic_id = Column(Integer, ForeignKey("learning_topics.id"))
    # This links the module back to its parent topic.
    topic = relationship("LearningTopic", back_populates="modules")
    # This links a module to its many tasks.
    tasks = relationship("LearningTask", back_populates="module", cascade="all, delete-orphan")

class LearningTask(Base):
    """Represents a single, actionable task, e.g., 'Watch a video on Python loops'."""
    __tablename__ = "learning_tasks"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    task_type = Column(String)  # "video", "article", "project"
    resource_url = Column(String)
    task_order = Column(Integer)
    module_id = Column(Integer, ForeignKey("learning_modules.id"))
    # This links the task back to its parent module.
    module = relationship("LearningModule", back_populates="tasks")