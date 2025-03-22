set -e
python monitoring/model_registry.py  
mlflow ui --host 0.0.0.0 --port 5000 & 
python monitoring/retrain_model.py
python monitoring/mlflow_tracking.py
python monitoring/drift_detection.py
