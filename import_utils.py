import pandas as pd

def read_csv(path):
    df = pd.read_csv(path)
    return df

def read_excel(path):
    df = pd.read_excel(path)
    return df

def read_parquet(path):
    df = pd.read_parquet(path)
    return df

def read_json(path):
    df = pd.read_json(path)
    return df