# Importing Libraries
import os
from pathlib import Path # This will change the format of the path of files when using in linux('/') or windows('\')
import logging

# Program for Logging ( INFO related log)
logging.basicConfig(level= logging.INFO, format="[%(asctime)s]: %(message)s:")

# src contains all the components of the project.
project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep", # Used when doing CI/CD deployment, Write CI/CD yaml file
    f'src/{project_name}/__init__.py', # init will help install local package. Install this folder as local package
    f'src/{project_name}/components/__init__.py', # This component is going to be another local package
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/common.py', # All utilities are going to be written here
    f'src/{project_name}/logging/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    'setup.py',
    'research/trials.ipynb',
    'test.py'
]

# Writing code to create the above files

for filepath in list_of_files:
    filepath = Path(filepath) # Path function changes the format of the filepath when using in linux('/') or windows('\')
    filedir, filename = os.path.split(filepath) # This will separate filedir and filename from filepath
    
    if filedir != "" :
        os.makedirs(filedir, exist_ok=True) # This will create all the directories in the file path
        logging.info(f"Created directory: {filedir} for the file: {filename}")       
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): # If you run template.py again, files will get
        with open(filepath, 'w') as f:                                     # created again and you will lose the original
            pass                                                           # file and programs written in it.
            logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
     