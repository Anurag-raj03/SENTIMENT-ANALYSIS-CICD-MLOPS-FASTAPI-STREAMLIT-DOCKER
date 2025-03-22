import pandas as pd
from sklearn.utils import resample

def balance_classes(df: pd.DataFrame):
    if 'Sentiment' not in df.columns:
        raise ValueError("Column 'Sentiment' not found in the dataset")
    
    df['Sentiment'] = df['Sentiment'].astype(str).str.strip().str.lower()
    
    neutral_df = df[df['Sentiment'] == "neutral"]
    positive_df = df[df['Sentiment'] == "positive"]
    negative_df = df[df['Sentiment'] == "negative"]

    print("Class distribution before resampling:")
    print("Neutral:", len(neutral_df), "Positive:", len(positive_df), "Negative:", len(negative_df))

    # Check if any class has 0 samples
    if len(neutral_df) == 0 or len(positive_df) == 0 or len(negative_df) == 0:
        raise ValueError("One or more sentiment classes have zero samples after preprocessing.")

    max_count = max(len(neutral_df), len(positive_df), len(negative_df))

    neutral_resampled = resample(neutral_df, replace=True, n_samples=max_count, random_state=42)
    positive_resampled = resample(positive_df, replace=True, n_samples=max_count, random_state=42)
    negative_resampled = resample(negative_df, replace=True, n_samples=max_count, random_state=42)

    balanced_df = pd.concat([neutral_resampled, positive_resampled, negative_resampled])
    balanced_df = balanced_df.sample(frac=1, random_state=42).reset_index(drop=True)

    balanced_df.to_csv("DATA/data_modified.csv", index=False)
    
    return balanced_df
