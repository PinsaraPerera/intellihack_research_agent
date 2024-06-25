import os
from pathlib import Path

project_name = "fastAPI_template"

list_of_files = [
    "app/__init__.py",
    "app/main.py",
    "app/api/__init__.py",
    "app/api/endpoints/__init__.py",
    "app/api/endpoints/users.py",
    "app/core/__init__.py",
    "app/core/config.py",
    "app/models/__init__.py",
    "app/models/user.py",
    "app/schemas/__init__.py",
    "app/schemas/user.py",
    "app/utils/__init__.py",
    "app/utils/hashing.py",
    "app/crud/__init__.py",
    "app/crud/user.py",
    "app/db/__init__.py",
    "app/db/base.py",
    "app/db/session.py",
    ".env",
    ".gitignore",
    "requirements.txt",
    "Dockerfile",
    "docker-compose.yml",
    "README.md",
    ".dockerignore",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass