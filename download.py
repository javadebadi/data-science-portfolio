"""
Date: 2022-09-12
Program: script to download datasets from sources which are used inside
this portfolio.
Author: Javad Ebadi
Email: javad.ebadi.1990@gmail.com
"""

import os
import requests
import zipfile
from pathlib import Path

# created data directory if not exists
os.makedirs('data', exist_ok=True)
# change current directory to data directory
os.chdir('data')

# a function to download file with given url
def download(url: str, filename: str = None):
    """A function to download file from url.

    Parameters
    ----------
    url : str
        The url of the file where the data resources is located.

    filename: str
        The name of the file to store in the data directory. If it is not 
        specified the function will try to guess the filename from given
        url.

    Returns
    -------
    filename : str
        Returns the filename at the end.
    """
    if filename is None:
        filename = url.split("/")[-1]
    filepath = os.path.join(".", filename)
    data = requests.get(url).content
    with open(filepath, 'wb') as f:
        f.write(data)
    return filename

def extract_zip_file(
    filename: str,
    extractd_directory_path: str,
    remove_original: bool = True,
    ):
    """Extract downladed zip files.

    Parameters
    ----------
    filename : str
        Name of the file in zip format inside the data directory.

    extractd_directory_path : str
        Name or path of the file or directory which we want to extract
        the zip file into it.

    remove_original : bool
        A boolean value determines wether to keep or delete the original
        zip file after the extraction is completed.

    Returns
    -------
    None
    """
    filepath = os.path.join(".", filename)
    with zipfile.ZipFile(filepath, 'r') as zip_ref:
        zip_ref.extractall(extractd_directory_path)
    if remove_original is True:
        os.remove(filepath)
    return None

def main():
    # stackoverflow data
    STACKOVERFLOW_2022_URL="https://info.stackoverflowsolutions.com/rs/719-EMH-566/images/stack-overflow-developer-survey-2022.zip"
    filename = download(STACKOVERFLOW_2022_URL)
    if filename.endswith('.zip'):
        extract_zip_file(filename, 'stackoverflow-developer-survey-2022')

if __name__ == '__main__':
    main()

