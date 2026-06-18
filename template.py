import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

list_of_files = [
    ".github/workflows/main.yaml",
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    "data/.gitkeep",
    "static/style.css",
    "templates/chat.html",
    "research/trials.ipynb",
    ".env",
    ".gitignore",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "store_index.py",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")