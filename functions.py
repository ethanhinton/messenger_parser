import pandas as pd
import os
import json

# Facebook encodes the message content incorrectly in the data dump, this function corrects this 
def fix_encoding(string):
    if type(string) == str:
        return string.encode('latin1').decode('utf8')
    else:
        return ""

# Parses all of the messages from a certain path.
# The path argument should be the full path to the "inbox" level of the FB data dump folder structure
# This should also work for "archived_threads" (although this was not tested)
def parse_messages(path, to_parquet=False, to_csv=False):

    conversations = []

    for conversation_name in os.listdir(path):
        folder_path = os.path.join(path, conversation_name)
        try:
            for message_file in os.listdir(folder_path):
                if message_file.endswith("json"):
                    with open(os.path.join(folder_path, message_file)) as f:
                        conversations.append(json.load(f))
        except NotADirectoryError:
            continue

    dataframes = []  
    for i, convo in enumerate(conversations):
        messages = convo['messages']
        df_messages = pd.DataFrame(messages)
        df_messages['title'] = convo['title']
        dataframes.append(df_messages)

    df_all_messages = pd.concat(dataframes)
    df_all_messages['content'] = df_all_messages['content'].apply(fix_encoding)

    if to_parquet:
        df_all_messages.to_parquet('messages.parquet', index=False)
    elif to_csv:
        df_all_messages.to_parquet('messages.csv', index=False)
    else:
        return df_all_messages
