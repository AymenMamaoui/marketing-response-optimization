import pandas as pd
from src.config import MARKETING_SEP, MARKETING_FILE, MARKETING_COLUMNS, AB_TEST_FILE, DATE_FORMAT, AB_TEST_COLUMNS, DATE_COL, AB_RENAMED_MAP, AB_TARGET, AB_INDEX_COL


# Validating the dataset
def validate_columns(df, expected, name):
    missing = set(expected) - set(df.columns)
    if missing:
        raise ValueError(f"[{name}] missing columns: {sorted(missing)}")

# Loading marketing dataset 
def load_marketing_campaign():
    marketing_data = pd.read_csv(MARKETING_FILE, sep=MARKETING_SEP)
    validate_columns(marketing_data, MARKETING_COLUMNS, "Marketing Dataset")
    marketing_data[DATE_COL] = pd.to_datetime(marketing_data[DATE_COL], format=DATE_FORMAT)
    
    return marketing_data

# Loading the A/B test Dataset
def load_ab_test():
    ab_data = pd.read_csv(AB_TEST_FILE)
    ab_data = ab_data.drop(columns=[AB_INDEX_COL])
    validate_columns(ab_data, AB_TEST_COLUMNS, "AB Test Dataset")
    ab_data = ab_data.rename(columns=AB_RENAMED_MAP)
    ab_data[AB_TARGET] = ab_data[AB_TARGET].astype(int)

    return ab_data



