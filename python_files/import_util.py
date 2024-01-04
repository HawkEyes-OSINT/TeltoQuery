import csv
import requests
from bs4 import BeautifulSoup

"""
Utility functions for importing data from a CSV file.
"""


def get_title(username):
    """
    Retreives the Telegram group/channel title from a given username.

    Args:
        username (str): The username of the Telegram group/channel.

    Returns:
        str: The title of the Telegram group/channel. None if the title cannot be found.
    """

    # get html
    url = f'https://t.me/{username}'
    response = requests.get(url)

    if response.status_code == 200:
        # get title
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('div', class_='tgme_page_title')

        return title.text.strip()
    
    else:
        return None
    

def get_data(filename):
    """
    Reads data from a CSV file and returns a list of lists containing the data.

    Args:
        filename (str): The name of the CSV file to read.

    Returns:
        list: A list of lists containing the data from the CSV file.
    """
    data = []

    with open(filename, 'r') as file:
        reader = csv.reader(file)

        # skip first two rows
        next(reader)
        next(reader)

        # get data from csv
        for row in reader:
            # ignore first column
            data.append(row[1:])

    return data


def usernames_to_titles(usernames):
    """
    Converts a list of lists of usernames to a list of lists of titles.

    Args:
        usernames (list): A list of lists of usernames.

    Returns:
        list: A list of lists of titles.
    """
    titles = []
    for username_list in usernames:
        title_list = []
        for username in username_list:
            if username:
                title_list.append(get_title(username))
        titles.append(title_list)

    return titles
