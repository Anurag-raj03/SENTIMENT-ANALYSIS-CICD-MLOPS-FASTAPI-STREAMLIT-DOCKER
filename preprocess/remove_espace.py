import pandas as pd
import re

def removesp(df: pd.DataFrame):
    for i in df.select_dtypes(include=['object']).columns:
        if i == "Sentence":
            pattern = r'\s+'
            df[i] = df[i].apply(lambda x: re.sub(pattern, ' ', str(x)).strip())
           
    return df
