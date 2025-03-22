import pandas as pd
import logging
import os 

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def data_vali(file_path: str):
    """Validates whether the file exists and is of the correct format."""
    
    if not os.path.exists(file_path):
        logging.error("File not found: %s", file_path)
        raise FileNotFoundError(f"File not found: {file_path}")

    if os.path.isdir(file_path):
        logging.error("Expected a file but received a directory: %s", file_path)
        raise IsADirectoryError(f"Expected a file but received a directory: {file_path}")

    ext = (".csv", ".xlsx")
    if not file_path.endswith(ext):
        logging.error("Invalid file format: %s. Only CSV and XLSX are supported.", file_path)
        raise ValueError("Unsupported file format. Only CSV and Excel files are allowed.")

    logging.info("File validation successful: %s", file_path)
    return file_path 
