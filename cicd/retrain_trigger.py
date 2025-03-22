import subprocess
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

print("Starting Model Retraining...")
result = subprocess.run(["python", "monitoring/retrain_model.py"], capture_output=True, text=True)
if result.returncode == 0:
    print("Model retraining complete.")
else:
    print("Error in retraining:", result.stderr)


