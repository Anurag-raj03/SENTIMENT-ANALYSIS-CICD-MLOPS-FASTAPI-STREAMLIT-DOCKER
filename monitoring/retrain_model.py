import os
import pandas as pd
import sys  
import logging
import mlflow
import mlflow.sklearn
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from preprocess.labeling import labe
from preprocess.remove_espace import removesp
from preprocess.removing_link import removing_links
from preprocess.remving_string import remove_unwanted_strings
from preprocess.making_lowerCase import preprocess_text
from preprocess.removing_no import rem_number
from preprocess.steme import apply_snowball_stemming_g
from preprocess.dropping_na import drop_in
from preprocess.resampl import balance_classes

mlflow.set_tracking_uri("http://mlflow:5000")
mlflow.set_experiment("My_Sentiment__Analysis-CICD-FINAL")

DATA_PATH = os.path.join("DATA", "data.csv")
MODEL_DIR = "Save_model"
EXAMPLE_INPUT_PATH = os.path.join("DATA", "mlflow_input_example.csv")
os.makedirs(MODEL_DIR, exist_ok=True)
MODEL_PATH = os.path.join(MODEL_DIR, "extra_trees.jbl")
VECTORIZER_PATH = os.path.join(MODEL_DIR, "tf_vectorizer.jbl")

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def retrain_model():
    try:
        logging.info("**Step 1: Loading Updated Dataset for Retraining**")
        df = pd.read_csv(DATA_PATH)
        if df is None or df.empty:
            raise ValueError("FAILED TO LOAD THE DATASET - FILE IS EMPTY OR MISSING")

        logging.info("**Step 2: Preprocessing the Updated Data**")
        df = removing_links(df)
        df = rem_number(df)                   
        df = remove_unwanted_strings(df)      
        df = removesp(df)                      
        df = preprocess_text(df)               
        df = apply_snowball_stemming_g(df, column_name='Sentence')
        df.to_csv("DATA/mlflow_modified.csv", index=False)

        df = balance_classes(df)  
        df.to_csv("DATA/mlflow_modified.csv", index=False)  
        df = pd.read_csv("DATA/mlflow_modified.csv")
        df = labe(df)

        if df.shape[0] < 50:
            logging.warning("Not enough data for retraining.")
            return
        
        logging.info("**Step 3: Splitting Data for Retraining**")
        split_idx = int(len(df) * 0.8)
        x_train, x_test = df["Sentence"][:split_idx], df["Sentence"][split_idx:]
        y_train, y_test = df["Sentiment"][:split_idx], df["Sentiment"][split_idx:]

        logging.info("**Step 4: Converting Text to TF-IDF Vectors**")
        vectorizer = TfidfVectorizer()
        x_train_vec = vectorizer.fit_transform(x_train)
        x_test_vec = vectorizer.transform(x_test)

        logging.info("**Step 5: Training the Extra Trees Model**")
        model = ExtraTreesClassifier()
        model.fit(x_train_vec, y_train)

        y_pred = model.predict(x_test_vec)
        acc = accuracy_score(y_test, y_pred)
        pre = precision_score(y_test, y_pred, average="weighted")
        rec = recall_score(y_test, y_pred, average="weighted")
        f1_s = f1_score(y_test, y_pred, average="weighted")

        logging.info(f"**Retraining completed successfully with model accuracy: {acc:.4f}**")

        joblib.dump(model, MODEL_PATH)
        joblib.dump(vectorizer, VECTORIZER_PATH)

        example_input = pd.read_csv(EXAMPLE_INPUT_PATH)
        example_vec = vectorizer.transform(example_input["Sentence"])
        example_input = pd.DataFrame(example_vec.toarray())
        logging.info("**Step 6: Logging Model, Metrics, and Input Example to MLflow**")
        with mlflow.start_run():
            mlflow.log_param("model_type", "ExtraTrees")
            mlflow.log_metric("accuracy", acc)
            mlflow.log_metric("precision", pre)
            mlflow.log_metric("recall", rec)
            mlflow.log_metric("f1_score", f1_s)

            mlflow.sklearn.log_model(model, "ExtraTreeClassifier", input_example=example_input)

            mlflow.log_artifact(VECTORIZER_PATH)
            mlflow.log_artifact(EXAMPLE_INPUT_PATH)

        logging.info("**New model, vectorizer, and input example saved and registered in MLflow.**")

    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
    except KeyError as e:
        logging.error(f"Missing column in dataset: {e}")
    except ValueError as e:
        logging.error(f"Value Error: {e}")
    except Exception as e:
        logging.error(f"Unexpected Error: {e}")

if __name__ == "__main__":
    retrain_model()
