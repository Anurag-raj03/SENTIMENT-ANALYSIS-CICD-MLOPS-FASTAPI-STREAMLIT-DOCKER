import pandas as pd

def preprocess_text(df: pd.DataFrame):
    if 'Sentence' in df.columns:
        df['Sentence'] = df['Sentence'].str.lower() 
       
    return df