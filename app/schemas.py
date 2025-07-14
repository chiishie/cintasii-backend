# app/schemas.py
from pydantic import BaseModel
from typing import List

# These schemas are for reading data from the database and returning it via the API.

class LearningTask(BaseModel):
    id: int
    title: str
    description: str
    task_type: str
    resource_url: str
    task_order: int

    class Config:
        from_attributes = True

class LearningModule(BaseModel):
    id: int
    title: str
    module_order: int
    tasks: List[LearningTask] = []

    class Config:
        from_attributes = True

class LearningTopic(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        from_attributes = True

# This is the main schema for the API response.
# It inherits from LearningTopic and adds the list of nested modules.
class LearningTopicDetail(LearningTopic):
    modules: List[LearningModule] = []