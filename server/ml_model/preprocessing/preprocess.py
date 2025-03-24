import numpy as np

def preprocess_data(df):
    df["Failure"] = np.where(df["Temperature"] > 45, 1, 0)
    return df