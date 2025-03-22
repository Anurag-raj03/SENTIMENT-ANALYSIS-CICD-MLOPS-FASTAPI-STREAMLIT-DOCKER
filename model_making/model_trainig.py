from sklearn.ensemble import ExtraTreesClassifier
from sklearn.metrics import accuracy_score
import joblib
import pandas as pd

def model_building(x_tfidf, y_train, x_test, y_test, vectorizer_path="Save_model/tf_vectorizer.jbl", save_path="Save_model/extra_trees.jbl"):
    tfidf_vectorizer = joblib.load(vectorizer_path)
    x_test_tfidf = tfidf_vectorizer.transform(x_test)
    etc = ExtraTreesClassifier()
    model = etc.fit(x_tfidf, y_train)
    y_pred = model.predict(x_test_tfidf)
    predicted_df = pd.DataFrame(y_pred, columns=["Predicted Sentiment"])
    predicted_df.to_csv("predictions.csv", index=False)

    accuracy = accuracy_score(y_test, y_pred) * 100
    print(f"Model Accuracy: {accuracy:.2f}%")
    

    if accuracy >= 75:
        joblib.dump(model, save_path)
        print(f"Model saved at {save_path}")
    else:
        print(" Model not saved. Accuracy is below 80%.")

    return accuracy

    
