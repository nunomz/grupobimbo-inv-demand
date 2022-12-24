import pandas as pd

#target is equal to the difference between the number of units of a given productthat were bought on a given week and the units of that same product that were returned the next week

def create_target(df):
    # if target = 0 then it stays the same, otherwise is converted to it's log10
    df.loc[df['target'] <= 0, 'target'] = 0
    df.loc[df['target'] > 0, 'target'] = np.log10(df["target"])
    # target mean
    meaner = np.mean(df["target"])
    # target to binary: if target bigger than its mean, then = 1 else = 0
    df.loc[df['target'] < meaner, 'target'] = 0
    df.loc[df['target'] > meaner, 'target'] = 1
    return df.groupby('target').size()/df['target'].count()