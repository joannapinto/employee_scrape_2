import pandas as pd

def load_reference_data(path):
    return pd.read_excel(path)

def load_raw_data(path):
    return pd.read_csv(path)

def filter_and_map_data(reference_df, raw_df):
    lookup_column = reference_df.columns[0]
    raw_column = raw_df.columns[0]
    unique_keys = raw_df[raw_column].drop_duplicates()
    return reference_df[reference_df[lookup_column].isin(unique_keys)]

def save_mapped_data(df, path):
    df.to_csv(path, index=False)

def run_scraper(url):
    print(f"Simulating download from: {url}")
