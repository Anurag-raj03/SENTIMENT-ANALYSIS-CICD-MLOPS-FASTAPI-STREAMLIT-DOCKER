import mlflow
import mlflow.sklearn
import joblib
import subprocess

MLFLOW_TRACKING_URI = "http://mlflow:5000" 

mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)

def check_model_performance():
    model_path = "./Save_model/extra_trees.jbl"
    model = joblib.load(model_path)

    experiment = mlflow.get_experiment_by_name("My_Sentiment__Analysis-CICD-FINAL")
    runs = mlflow.search_runs(experiment_ids=[experiment.experiment_id])
    if runs.empty:
        print("No previous runs found. Training a new model...")
        return False
    latest_run = runs.iloc[0]
    accuracy = latest_run["metrics.accuracy"]
    print(f"Latest Model Accuracy: {accuracy}")
    if accuracy < 0.80:
        print("Accuracy dropped below 80%! Triggering retraining...")
        result = subprocess.run(["python", "cicd/retrain_trigger.py"], capture_output=True, text=True)

        if result.returncode == 0:
            print("Retraining completed successfully!")
        else:
            print(f"Error in retraining: {result.stderr}")

        return True

    print("Model performance is acceptable. No retraining needed.")
    return False

if __name__ == "__main__":
    check_model_performance()
