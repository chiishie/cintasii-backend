
# Cintasii Education - Backend API

This is the backend server for the Cintasii Education application, a personalized learning path generator. It is built with FastAPI and uses a SQLite database to store and serve pre-curated learning plans.

## Core Functionality

* Serves a list of available learning topics (e.g., "Python for Data Science").
* Provides a complete, structured learning plan for a selected topic, including modules and actionable tasks.
* Simulates an AI-powered generator by serving high-quality, pre-populated data.

---

## Prerequisites

Before you begin, ensure you have the following installed:

* **Python 3.8+**: [Download Python](https://www.python.org/downloads/)
* **pip**: Python's package installer (usually comes with Python)

---

## 🚀 Step-by-Step Setup and Installation

Follow these steps to get the backend running locally.

### 1. Clone the Repository

If your project is on Git, clone it. Otherwise, ensure you are in the project's root directory (`cintasii-backend`).

### 2. Create and Activate a Virtual Environment

It is highly recommended to use a virtual environment to manage project dependencies.

* **Create the environment:**
    ```bash
    python3 -m venv venv
    ```

* **Activate the environment:**
    * On **macOS/Linux**:
        ```bash
        source venv/bin/activate
        ```
    * On **Windows**:
        ```bash
        .\venv\Scripts\activate
        ```
    Your terminal prompt should now be prefixed with `(venv)`.

### 3. Install Dependencies

Install all the required Python packages from the `requirements.txt` file.

```bash
pip install -r requirements.txt
````

### 4. Populate the Database

For the MVP, the learning plans are pre-curated. A script is provided to create the database and populate it with the initial learning plan data.

**Run this script once.** If you encounter an error, follow the troubleshooting steps below.

```bash
python create_db_data.py
```

This will create a `cintasii_learning.db` file in your project directory and fill it with the necessary data.

### Troubleshooting Step 4

If the script fails or the server has no data, follow these steps:

1.  **Confirm your location**: Make sure you are in the `cintasii-backend` root folder. Your `create_db_data.py` file should be visible when you list files (`ls` on Mac/Linux or `dir` on Windows).
2.  **Check your virtual environment**: Ensure your terminal prompt begins with `(venv)`. If not, reactivate it using the commands in Step 2.
3.  **Reset the database**: Delete the `cintasii_learning.db` file from your directory if it exists. This ensures you start with a clean slate.
4.  **Re-run the script**:
    ```bash
    python create_db_data.py
    ```
    You should see output messages like "Creating database tables..." and "Database populated successfully\!".

-----

## ▶️ Step 5: Run the Server

Once the setup is complete and the database is populated, you can start the FastAPI server.

```bash
uvicorn app.main:app --reload
```

  * `uvicorn app.main:app`: Tells the Uvicorn server to run the `app` object from the `main.py` file inside the `app` directory.
  * `--reload`: Enables auto-reload, which automatically restarts the server whenever you save a code change.

The server will now be running at **https://www.google.com/search?q=http://127.0.0.1:8000**.

-----

## 📚 API Endpoints

The server provides interactive API documentation (powered by Swagger UI). To explore and test the endpoints, open your web browser and navigate to:

[**http://127.0.0.1:8000/docs**](https://www.google.com/search?q=http://127.0.0.1:8000/docs)

### Main Endpoints:

  * `GET /api/topics`

      * **Description**: Retrieves a list of all available learning topics. The frontend uses this to display the initial topic selection screen.
      * **Example Response**:
        ```json
        [
          {
            "id": 1,
            "name": "Python for Data Science",
            "description": "A complete curriculum..."
          }
        ]
        ```

  * `GET /api/learning-plans/{topic_id}`

      * **Description**: Retrieves a complete, nested learning plan for a specific topic ID. This is the core endpoint that provides the daily task breakdown.
      * **Example Response (for topic\_id=1)**:
        ```json
        {
          "id": 1,
          "name": "Python for Data Science",
          "description": "A complete curriculum...",
          "modules": [
            {
              "id": 1,
              "title": "Week 1: Python Fundamentals",
              "module_order": 1,
              "tasks": [
                {
                  "id": 1,
                  "title": "Install Python & VS Code",
                  "description": "Set up your development environment.",
                  "task_type": "article",
                  "resource_url": "https://...",
                  "task_order": 1
                }
              ]
            }
          ]
        }
        ```

<!-- end list -->

```
```
