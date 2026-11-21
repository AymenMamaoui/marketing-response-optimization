import pandas as pd
from src.config import ID_COL, TARGET, TEST_FILE, TRAIN_FILE, TEST_SIZE, RANDOM_STATE
from sklearn.model_selection import train_test_split

def remove_duplicate_customers(df: pd.DataFrame) -> pd.DataFrame:
    """Drop customers duplicated on every column except the ID (keep the first occurrence)."""
    feature_cols = [c for c in df.columns if c != ID_COL]
    return df.drop_duplicates(subset=feature_cols, keep="first").reset_index(drop=True)

def split_data(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Returns (train, test)"""
    train_df, test_df = train_test_split(
    df, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=df[TARGET]
    )   
    return train_df, test_df

def save_splits(train: pd.DataFrame, test: pd.DataFrame) -> None:
    """Save splits (train and test) in data/processed"""
    train.to_csv(TRAIN_FILE, index=False)
    test.to_csv(TEST_FILE, index=False)