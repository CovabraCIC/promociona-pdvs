import pandas as pd


def difference(df1:pd.DataFrame, df2:pd.DataFrame):
    """Compare dois DataFrames e receba a divergência entre eles."""	
    dif = df2[~df2.apply(tuple, axis=1).isin(df1.apply(tuple, axis=1))].reset_index(drop=True)
    return dif
