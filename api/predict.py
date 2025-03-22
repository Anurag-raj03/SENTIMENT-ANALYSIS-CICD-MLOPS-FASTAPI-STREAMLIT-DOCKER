import joblib as j
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

model = j.load('Save_model/extra_trees.jbl')
vec = j.load('Save_model/tf_vectorizer.jbl')

def predict_sentiment(text: str):
    text_tfidf = vec.transform([text])
    pred = model.predict(text_tfidf)[0]
    return int(pred)  
