# intellihack micro services API
This is the research agent powered UP with most capable GPT-4o model to do the research using several tools like web searching , web scraping and access research document databases.

![alt text](image.png)

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [License](#license)

## Introduction
This is a backend project built with FastAPI. The project provides several routing paths to handle different functionalities. FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

## Features
- Fast and asynchronous API endpoints.
- Detailed API documentation with Swagger UI and Redoc.
- Easy to extend and customize.
- Uses Pydantic for data validation.

## Installation

### Prerequisites
- Python 3.6+
- `pip` (Python package installer)

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/PinsaraPerera/intellihack_research_agent.git
    cd your-repo-name
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration
Create a `.env` file in the root directory and add your environment variables. Example:

```bash
PROJECT_ID = ""
REGION = ""
INSTANCE_NAME = ""
INSTANCE_CONNECTION_NAME = f"{PROJECT_ID}:{REGION}:{INSTANCE_NAME}"
DB_USER = ""
DB_PASS = ""
DB_NAME = ""
PRIVATE_IP = 
OPENAI_API_KEY = ""
BUCKET_NAME = ""

BROWSERLESS_API_KEY = ""
SERPER_API_KEY = ""
```

## Running the Application
To run the application, execute the following command:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 80 --reload
```

This will start the server at http://127.0.0.1:80

API Documentation
FastAPI automatically generates interactive API documentation at the following URLs:

Swagger UI: http://127.0.0.1:80/docs
Redoc: http://127.0.0.1:80/redoc

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
