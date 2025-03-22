from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import joblib
import os
def vec_conv(x_train: pd.Series, y_train: pd.Series, save_path="Save_model/tf_vectorizer.jbl"):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    tf = TfidfVectorizer()
    x_tfidf = tf.fit_transform(x_train)
    joblib.dump(tf, save_path)
    
    return x_tfidf, y_train