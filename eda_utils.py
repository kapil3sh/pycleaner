

def describe_df(df):
    print(df.describe())
    return df.describe()


def check_null(df):
    print(df.isnull.sum(axis=0))
    return df.isnull.sum(axis=0)

def get_info(df):
    print(df.info())
    return df.info()

