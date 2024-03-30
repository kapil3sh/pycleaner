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

def file_import(path):
    path = path

    if '.csv' in path :
        return read_csv(path)
    elif ('.xlsx' in path ) or ('.xls' in path) :
        return read_excel(path)
    elif ('.parquet' in path) or ('.pqt' in path):
        return read_parquet(path)
    elif '.json' in path:
        return read_json(path)