# Configurations
"""This file should contain the informations about :
        - Dataset's (both raw and processed) paths
        - column's name of each dataset
        - column's separator
        - date format
        - Our target
        - new columns names in case we rename them 
"""
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]   # project root

RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"

PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"

MARKETING_FILE = RAW_DATA_DIR / "marketing_campaign.csv"
AB_TEST_FILE =  RAW_DATA_DIR / "marketing_AB.csv"
MARKETING_SEP = ";"
DATE_FORMAT = "%Y-%m-%d"


RANDOM_STATE = 42

TARGET = "Response"

ID_COL = "ID"

DATE_COL = "Dt_Customer"

CATEGORICAL_COLS = ['Education', 'Marital_Status']

NUMERICAL_COLS = ['Year_Birth', 'Income', 'Kidhome', 'Teenhome', 'Recency', 'MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds', 'NumDealsPurchases', 'NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases', 'NumWebVisitsMonth']

PAST_CAMPAIGN_COLS = ['AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5', 'AcceptedCmp1', 'AcceptedCmp2']

BINARY_COLS = PAST_CAMPAIGN_COLS + ["Complain"]

CONSTANT_COLS = ['Z_CostContact', 'Z_Revenue']

MARKETING_COLUMNS = [ID_COL, TARGET, DATE_COL] + CATEGORICAL_COLS + BINARY_COLS + CONSTANT_COLS + NUMERICAL_COLS 
assert len(MARKETING_COLUMNS) == 29 # just to make sure that the number of columns is correct after importing

AB_RENAMED_MAP = {"user id":"user_id", "test group":"test_group", "converted":"converted", "total ads":"total_ads", "most ads day":"most_ads_day", "most ads hour": "most_ads_hour"}
AB_TEST_COLUMNS = list(AB_RENAMED_MAP) # AB_TEST_COLUMNS WILL CONTAIN JUST THE KEYS(WHICH ARE THE ORIGINAL NAMES OF THE COLUMNS) NOT THE VALUES
AB_GROUP_COL = "test_group"
AB_TARGET = "converted"
AB_INDEX_COL = "Unnamed: 0"