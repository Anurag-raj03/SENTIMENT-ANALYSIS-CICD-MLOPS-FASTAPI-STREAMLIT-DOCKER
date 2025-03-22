import sys
import os
import subprocess
import pandas as pd
from scipy.stats import ks_2samp

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from databases.db_config import get_connection
def detect_drift(threshold=0.3):
    conn = get_connection()
    query = "SELECT Sentiment FROM sentiment_data"
    df = pd.read_sql_query(query, conn)
    conn.close()
    if df.shape[0] < 50:
        print("Not Enough Data to detect drift.")
        return False
    split_idx = int(len(df) * 0.80)
    old_data = df.iloc[:split_idx]["Sentiment"]
    recent_data = df.iloc[split_idx:]["Sentiment"]
    stat, p_value = ks_2samp(old_data, recent_data)

    if p_value < threshold:
        print("Drift Detected in Sentiment Data! Triggering Retraining...")
        result = subprocess.run(["python", "monitoring/retrain_model.py"], capture_output=True, text=True)

        if result.returncode == 0:
            print("Model retraining completed successfully!")
        else:
            print(f"Error in retraining: {result.stderr}")

        return True
    else:
        print("No drift detected. Model remains unchanged.")
        return False

if __name__ == "__main__":
    detect_drift()
