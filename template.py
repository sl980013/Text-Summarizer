import os
from pathlib import Path
# to log information
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

# project name
name = "textSummarizer"

# list of files
file_list = [
    ".github/workflows/.gitkeep",
    f"src/{name}/__init__.py",
    f"src/{name}/components/__init__.py", #constructors file
    f"src/{name}/utils/__init__.py",
    f"src/{name}/utils/common.py",
    f"src/{name}/logging/__init__.py",
    f"src/{name}/config/__init__.py",
    f"src/{name}/config/configuration.py",
    f"src/{name}/pipeline/__init__.py",
    f"src/{name}/entity/__init__.py",
    f"src/{name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "test.py"
]

for filepath in file_list:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Created file: {filepath}")

    else:
        logging.info(f"File already exists: {filepath}")