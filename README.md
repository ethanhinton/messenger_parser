# Messenger Parser
A program to parse Facebook Messenger data from the JSON download folder structure and present in a pandas DataFrame.

## Using the Code
1. Import the two parse_messages and fix_encoding functions from the functions.py file.
2. Pass the full path to the "inbox" subfolder in the Facebook data dump folder structure as the *path* argument in the parse_messages function.
3. Specify whether the DataFrame should be written to parquet (*to_parquet=True*), or to csv (*to_csv=True*), or do not specify to return the DataFrame as the function output.
