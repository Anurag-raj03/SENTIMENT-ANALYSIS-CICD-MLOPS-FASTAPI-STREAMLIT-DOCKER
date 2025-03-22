import pandas as pd

def labe(df: pd.DataFrame):
    if 'Sentiment' in df.columns:
        df['Sentiment'] = df['Sentiment'].astype(str).str.strip().str.lower()
        df['Sentiment'] = df['Sentiment'].apply(
            lambda x: 1 if 'po' in x else 0 if 'neu' in x else 2 if 'neg' in x else None
        )
        print("Unique Sentiment Values After Mapping:", df['Sentiment'].unique())
        df.dropna(subset=['Sentiment'], inplace=True)
        

    return df
