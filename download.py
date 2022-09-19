"""
Date: 2022-09-12
Program: script to download datasets from sources which are used inside
this portfolio.
Author: Javad Ebadi
Email: javad.ebadi.1990@gmail.com
"""

import os
from data_engineering import extract

# created data directory if not exists
os.makedirs('data', exist_ok=True)
# change current directory to data directory
os.chdir('data')

def main():
    extract.main()

if __name__ == '__main__':
    main()

