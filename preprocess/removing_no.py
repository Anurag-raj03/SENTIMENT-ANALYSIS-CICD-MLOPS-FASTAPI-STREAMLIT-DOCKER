import pandas as pd
import re as r

def rem_number(df:pd.DataFrame):
    for i in df.select_dtypes(include=['object']).columns:
        if i=='Sentence':
           pattern=r"\d+"  
           df[i]=df[i].apply(lambda x: r.sub(pattern,'',str(x)))
    return df       