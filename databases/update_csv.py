import pandas as pd
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from databases.db_config import get_connection  

CSV_PATH = "DATA/data.csv"

def updated_csv():
    conn = get_connection()
    query = "SELECT * FROM sentiment_data"
    df = pd.read_sql_query(query, conn)
    conn.close()

    df.to_csv("DATA/data.csv", index=False, mode='a', header=not os.path.exists("DATA/data.csv"))
    print(f"✅ DATA Exctracted from the DataBase and saved to MAIN CSV file updated : {CSV_PATH}")
    
    print(" :) If the docker container restart  it will auto retrain the model if drift or the model accuracy Drop than 75% (:")

if __name__ == "__main__":
    updated_csv()
