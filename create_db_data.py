# create_db_data.py
from app.database import SessionLocal, engine
from app import models

# Create the database tables
print("Creating database tables...")
models.Base.metadata.create_all(bind=engine)
print("Done.")

db = SessionLocal()

# --- Check if data already exists ---
if db.query(models.LearningTopic).first():
    print("Database already contains data. Skipping population.")
else:
    print("Populating database with learning plan...")
    # --- Create the Main Topic ---
    python_topic = models.LearningTopic(
        name="Python for Data Science",
        description="A complete curriculum to take you from zero to a competent Python data analyst."
    )
    db.add(python_topic)
    db.commit()

    # --- Create Modules ---
    module1 = models.LearningModule(title="Week 1: Python Fundamentals", module_order=1, topic_id=python_topic.id)
    module2 = models.LearningModule(title="Week 2: Data Manipulation with NumPy & Pandas", module_order=2, topic_id=python_topic.id)
    db.add_all([module1, module2])
    db.commit()

    # --- Create Tasks for Module 1 ---
    task1_1 = models.LearningTask(title="Install Python & VS Code", description="Set up your development environment.", task_type="article", resource_url="https://code.visualstudio.com/docs/python/python-tutorial", task_order=1, module_id=module1.id)
    task1_2 = models.LearningTask(title="Watch: Python for Beginners", description="A comprehensive 4-hour video course covering the basics.", task_type="video", resource_url="https://www.youtube.com/watch?v=rfscVS0vtbw", task_order=2, module_id=module1.id)
    task1_3 = models.LearningTask(title="Project: Simple Calculator", description="Apply your knowledge of variables and functions to build a calculator.", task_type="project", resource_url="https://www.freecodecamp.org/news/python-projects-for-beginners/#simple-calculator-project", task_order=3, module_id=module1.id)
    db.add_all([task1_1, task1_2, task1_3])

    # --- Create Tasks for Module 2 ---
    task2_1 = models.LearningTask(title="Watch: NumPy Explained in 5 Minutes", description="A quick introduction to the fundamental library for scientific computing.", task_type="video", resource_url="https://www.youtube.com/watch?v=xECXZ3tyONo", task_order=1, module_id=module2.id)
    task2_2 = models.LearningTask(title="Read: 10 Minutes to pandas", description="The official, quick-start guide to the Pandas library.", task_type="article", resource_url="https://pandas.pydata.org/docs/user_guide/10min.html", task_order=2, module_id=module2.id)
    task2_3 = models.LearningTask(title="Project: Analyze Titanic Dataset", description="Perform a basic exploratory data analysis on a real dataset.", task_type="project", resource_url="https://www.kaggle.com/code/alexisbcook/titanic-tutorial", task_order=3, module_id=module2.id)
    db.add_all([task2_1, task2_2, task2_3])

    db.commit()
    print("Database populated successfully!")

db.close()