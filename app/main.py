# app/main.py
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

from . import crud, models, schemas
from .database import engine, get_db

# This line ensures the tables are created if they don't exist when the app starts.
# models.Base.metadata.create_all(bind=engine) # We do this in the script now.

app = FastAPI(title="Cintasii Education API")

# --- CORS Middleware ---
# This allows your React frontend to communicate with this backend.
origins = [
    "http://localhost:3000", # Default for Create React App
    "http://localhost:5173", # Default for Vite
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- API Endpoints ---
@app.get("/api/topics", response_model=List[schemas.LearningTopic])
def read_topics(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Endpoint to get the list of available learning topics for the dropdown."""
    topics = crud.get_topics(db, skip=skip, limit=limit)
    return topics

@app.get("/api/learning-plans/{topic_id}", response_model=schemas.LearningTopicDetail)
def read_learning_plan(topic_id: int, db: Session = Depends(get_db)):
    """The main endpoint to fetch a complete learning plan."""
    db_plan = crud.get_topic_with_details(db, topic_id=topic_id)
    if db_plan is None:
        raise HTTPException(status_code=404, detail="Topic not found")
    return db_plan