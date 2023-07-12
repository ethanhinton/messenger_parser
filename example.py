from functions import *

PATH = "messages/inbox/"

if __name__ == "__main__":
    parse_messages(PATH, to_parquet=True)

