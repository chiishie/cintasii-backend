# app/crud.py
from sqlalchemy.orm import Session, joinedload
from . import models

def get_topics(db: Session, skip: int = 0, limit: int = 10):
    """Fetches a list of all available learning topics."""
    return db.query(models.LearningTopic).offset(skip).limit(limit).all()

def get_topic_with_details(db: Session, topic_id: int):
    """
    Fetches a single topic and all its related modules and tasks.
    'joinedload' is a performance optimization that tells SQLAlchemy to fetch
    the related data in a single, more efficient query.
    """
    return db.query(models.LearningTopic).options(
        joinedload(models.LearningTopic.modules).joinedload(models.LearningModule.tasks)
    ).filter(models.LearningTopic.id == topic_id).first()