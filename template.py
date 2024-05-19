import os
from pathlib import Path

list_of_files = [
    "QAWITHPDF/__init__.py",
    "QAWITHPDF/data_ingestion.py",
    "QAWITHPDF/embedding.py",
    "QAWITHPDF/model_api.py",
    "Experiments/experiment.ipynb",
    "StreamlitApp.py",
    "logger.py",
    "exception.py",
    "setup.py"
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        #logging.info(f"Creating directory; {filedir} for file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            #logging.info(f"Creating empty file:{filepath}")

    #else:
        #logging.info(f"{filename} is already created")