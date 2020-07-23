from sklearn.preprocessing import scale
import pandas as pd

def normalize(df):
    ''' Normalize a dataframe using sklearn's preprocessor, but retaining the columns information'''

    cols = [col for col in df.columns]
    std_df = pd.DataFrame(scale(df))
    print(type(cols))
    #std_df.rename(columns=*columns, inplace=True)

    return std_df
