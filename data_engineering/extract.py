"""
Date: 2022-09-18
Program: script to download stackoverflow surveys dataset.
Author: Javad Ebadi
Email: javad.ebadi.1990@gmail.com
"""

import requests
from bs4 import BeautifulSoup
import os
import requests
import zipfile
from pathlib import Path


STACKOVERFLOW_DEVELOPERS_SURVEY_DATASET_URL = 'https://insights.stackoverflow.com/survey'

def fetch_datasets_page():
    """fetchs and returns html content from stackoverflow url.
    """
    survey_response = requests.get(STACKOVERFLOW_DEVELOPERS_SURVEY_DATASET_URL)
    if survey_response.status_code == 200:
        survey_html = requests.get(STACKOVERFLOW_DEVELOPERS_SURVEY_DATASET_URL).content
    else:
        raise RuntimeError(
            f"Couldn't fetch Stack Overflow dataset from url: "
            f"'{STACKOVERFLOW_DEVELOPERS_SURVEY_DATASET_URL}'"
            )
    return survey_html

def get_dataset_links_from_page(html_string: str, filter_string):
    """Gets all hrefs of anchors tags from html string.
    
    The function first gets all anchor tags from `html_string` and then
    returns list of hrefs of these anchors tag that pass the `filter_string`.

    Parameters
    ----------
    html_string : str
        The content of an html document.

    filter_string : str
        An string that is desired to exist in all hrefs which will be 
        returned.

    Returns
    -------
    : list
        Returns list of URLs (strings).
    """
    soup = BeautifulSoup(html_string, 'html.parser')
    anchors = soup.find_all('a')
    return [anchor['href'] for anchor in anchors if (filter_string in anchor['href'])]


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
    survey_html = fetch_datasets_page()
    datasets_urls = get_dataset_links_from_page(survey_html, '.zip')
    for url in datasets_urls:
        filename = download(url)
        extracted_dir = filename.replace(".zip", "")
        extract_zip_file(filename, extracted_dir)
