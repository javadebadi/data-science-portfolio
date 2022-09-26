"""
Date: 2022-09-19
Program: script to transform stackoverflow surveys dataset.
Author: Javad Ebadi
Email: javad.ebadi.1990@gmail.com
"""

import pandas as pd

df = pd.read_csv('./data/stack-overflow-developer-survey-2011/2011 Stack Overflow Survey Results.csv')
print(df.columns)


def main():
    print(df.columns)