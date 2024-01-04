import import_util
import output_util

"""
Create a query to search for keywords in channels.
"""

def create_query(keywords, channels):
    """
    Write query to search for keywords in channels.
    :param keywords: list of keywords to search for
    :param channels: list of channels to search in
    :return: query to search for keywords in channels, as a string.
    """
    query = "(("

    for keyword in keywords:
        query += "("
        for key in keyword:
            if key:
                query += f'"{key}" AND '
        query = query[:-4] + ") OR "

    query = query[:-4] + ")" + " AND site:telegram"

    if channels:
        query += " AND category:("
        for channel in channels:
            query += "("
            for chan in channel:
                if chan:
                    query += f'"{chan}" AND '
            query = query[:-4] + ") OR "

        query = query[:-4] + "))"

    return query


keywords = import_util.get_data('keywords.csv')
channels = import_util.get_data('channels.csv')
channels = import_util.usernames_to_titles(channels)
output_util.append_to_file(create_query(keywords, channels))

