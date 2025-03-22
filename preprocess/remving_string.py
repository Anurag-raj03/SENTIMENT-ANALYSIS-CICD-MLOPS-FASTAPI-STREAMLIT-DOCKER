import pandas as pd
import re

def remove_unwanted_strings(df: pd.DataFrame):
    for col in df.select_dtypes(include=['object']).columns:
        if col == "Sentence": 
            pattern = r"[@#\$%^&\*\(\)_\+=\{\}\[\]:;\"'<>,\.\?/\\|~`]" 
            df[col] = df[col].apply(lambda x: re.sub(pattern, '', str(x)).strip())  
    return df