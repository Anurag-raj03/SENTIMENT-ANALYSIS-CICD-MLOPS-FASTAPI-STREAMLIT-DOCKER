import pandas as pd
import nltk
from nltk.stem import SnowballStemmer
snowball = SnowballStemmer("english")
def apply_snowball_stemming_g(df: pd.DataFrame, column_name: str):
    if column_name in df.columns:
        df[column_name] = df[column_name].apply(lambda x: ' '.join([snowball.stem(word) for word in str(x).split()]))
    return df 