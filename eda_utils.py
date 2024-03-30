import pandas as pd
import io

def describe_df(df):
    print(df.describe())
    return df.describe()


def check_null(df):
    print(df.isnull().sum())
    return df.isnull().sum()

def get_info(df):
    buffer = io.StringIO()
    df.info(buf=buffer)
    lines = buffer.getvalue().splitlines()
    new_df = (pd.DataFrame([x.split() for x in lines[5:-2]], columns=lines[3].split())
       .drop('Count',axis=1)
       .rename(columns={'Non-Null':'Non-Null Count'}))
    return (new_df)


