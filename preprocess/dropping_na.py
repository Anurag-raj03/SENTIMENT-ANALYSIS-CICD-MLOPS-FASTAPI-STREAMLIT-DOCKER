import pandas as pd
def drop_in(df:pd.DataFrame):
    df=df.dropna()
    return df
    