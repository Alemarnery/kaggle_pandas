import pandas as pd


def index():
    file = "./data/winemag-data-130k-v2.csv"
    return pd.read_csv(file, index_col=0)
