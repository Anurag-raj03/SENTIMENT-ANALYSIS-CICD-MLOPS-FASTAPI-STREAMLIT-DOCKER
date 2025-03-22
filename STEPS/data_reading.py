import pandas as pd
import logging
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_validation import data_vali

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def read_f(file_path: str):
    """Reads a CSV or Excel file after validation."""
    file_path = data_vali(file_path)  

    try:
        if file_path.endswith(".csv"):
            df = pd.read_csv(file_path)
        elif file_path.endswith(".xlsx"):
            df = pd.read_excel(file_path)
        else:
            logging.error("Unsupported file format: %s", file_path)
            raise ValueError("Unsupported file format. Only CSV and Excel files are allowed.")

        logging.info("File '%s' read successfully with shape: %s", file_path, df.shape)
        return df    

    except Exception as e:
        logging.error("Error reading the file: %s", e)
        raise
