
# TeltoQuery

## Overview

This Python tool helps you generate queries for CyberSixGill based on keywords and Telegram channels/groups. The tool requires user input for keywords and channel/group usernames using CSV files.

## Setup

### 1. Clone the Repository


    git clone https://github.com/your-username/TeltoQuery.git
    cd TeltoQuery

2. Install Python

    Make sure you have Python installed on your machine. If not, download and install it from python.org.

3. Input Keywords

    Edit the keywords.csv file in the repository:

    Each row in the CSV represents an "and" condition, and each column represents an "or" condition.

4. Input Channels/Groups

    Edit the channels.csv file in the repository:

    Just like with keywords, each row in the CSV represents an "and" condition, and each column represents an "or" condition.
    Usage

Run the script:

    Windows: Double-click the run_program.bat file in the python_files folder.

    Linux/Mac: Open a terminal, navigate to the project folder, and run:

    bash

    chmod +x python_files/run_program.sh
    ./python_files/run_program.sh

The generated queries will be saved in the queries.txt file.

Open the queries.txt file to view the generated queries.

Creating a Shortcut (Optional)

For convenience, you can create a shortcut to run the script:

    Windows:
        Right-click on python_files/run_program.bat.
        Select "Create shortcut."
        Move the shortcut to your desktop or preferred location.

    Linux/Mac:
        Right-click on python_files/run_program.sh.
        Select "Create Launcher" or "Make Link."
        Move the shortcut to your desktop or preferred location.

Important Notes

    Always ensure that your Python installation is up to date.
    Review the keywords.csv and channels.csv files carefully to ensure correct input format.
    Be cautious while running scripts from unknown sources. Verify the contents of the script before execution.

Troubleshooting

If you encounter any issues, please open an issue on the GitHub repository.