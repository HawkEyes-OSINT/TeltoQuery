from datetime import datetime
import os

"""
Utility method for export
"""

def append_to_file(query):
    """
    Write the query to a file.
    
    Args:
        query (str): The query to write to the file.
    
    Returns:
        None
    """
    # get the current date and time
    dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # prepare content to append
    content = f"\n\n{dt}\n{query}"

    # append to the file
    output_file = os.path.join(os.path.dirname(__file__), '../queries.txt')
    with open(output_file, "a") as file:
        file.write(content)

    return
