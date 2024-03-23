import pandas as pd


# load excel file
def load_data(file):
    """"
    Load data from URI
    """
    df = pd.read_csv(file)
    return df


def prepare_excel_data(df):
    """
    Make data column to lowercase
    """
    df.columns = [x.replace(' ', '_').lower() for x in df.columns]
    return df


# Read document
def read_document(path):
    with open(path) as f:
        bbc_news = f.read()
    return bbc_news
