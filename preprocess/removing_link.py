import re as r
import pandas as pd

def removing_links(df:pd.DataFrame):
    for i in df.select_dtypes(include=['object']).columns:
        if i=='Sentence':
            pattern = r"https?://\S+|www\.\S+"
            df[i]=df[i].apply(lambda x: r.sub(pattern,'',str(x)))
    return df   


        