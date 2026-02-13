import os
from pathlib import Path

project_name = "multi_agent"

list_of_files = [
    f"{project_name}/__init__.py",

    f"{project_name}/exception/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/logger/__init__.py",

    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_loader.py",
    f"{project_name}/components/text_extractor.py",
    f"{project_name}/components/chunker.py",
    f"{project_name}/components/embedder.py",
    f"{project_name}/components/vector_store.py",
    f"{project_name}/components/retriever.py",
    f"{project_name}/components/generator.py",

    f"{project_name}/client/__init__.py",

    f"{project_name}/reader/__init__.py",
    f"{project_name}/reader/pdf_docs_reader.py",
    f"{project_name}/reader/image_reader.py",
    f"{project_name}/reader/youtube_link_reader.py",

    f"{project_name}/pipeline/__init__.py",

    f"{project_name}/caching/__init__.py",

    f"{project_name}/config/__init__.py",
    f"{project_name}/config/mongodb_config.py",

    "notebook/Research_notebook.ipynb",


    f"{project_name}/",
    f"{project_name}/",
    "setup.py",
    "requirements.txt",
    ".env",
    ".gitignore",
    "app.py",
    "demo.py",
]


for filepath in list_of_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok= True)

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    
    else:
        print(f" File is already present at {filepath}")