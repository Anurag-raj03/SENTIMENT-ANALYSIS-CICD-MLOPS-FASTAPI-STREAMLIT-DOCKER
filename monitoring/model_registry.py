import mlflow
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def register_model():
    mlflow.set_tracking_uri("http://mlflow:5000")
    experiment_name = "My_Sentiment__Analysis-CICD-FINAL"
    if not mlflow.get_experiment_by_name(experiment_name):
        experiment_id = mlflow.create_experiment(experiment_name)
        print(f"✅ Experiment '{experiment_name}' created with ID: {experiment_id}")
    else:
        experiment_id = mlflow.get_experiment_by_name(experiment_name).experiment_id
        print(f"ℹ️ Using existing experiment '{experiment_name}' (ID: {experiment_id})")
    mlflow.set_experiment(experiment_name)
    client = mlflow.tracking.MlflowClient()
    runs = client.search_runs(experiment_id, order_by=["start_time DESC"], max_results=1)
    if not runs:
        print("No recent runs found with a logged model.")
        return
    latest_run_id = runs[0].info.run_id
    model_uri = f"runs:/{latest_run_id}/ExtraTreeClassifier"
    model_version = mlflow.register_model(model_uri=model_uri, name="Sentiment_twitter_Model")
    print(f"✅ Model registered successfully as version {model_version.version}")
if __name__ == "__main__":
    register_model()
