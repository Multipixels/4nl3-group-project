# README - Data

> **This document deals with the categorization of toxic content and messages found online that contain profane, vulgar, or offensive content. Proceed with caution.**

## Raw Data

Data Source: <https://www.kaggle.com/datasets/romovpa/gosuai-dota-2-game-chats> 

To access the data source, you can download it from the link above or use the command below:

`curl -L gosuai-dota-2-game-chats.zip https://www.kaggle.com/api/v1/datasets/download/romovpa/gosuai-dota-2-game-chats`

## Data

Data was cleaned and reformatted it into a JSON format. Any games with foreign text was removed, and game IDs were relabeled. The JSON file indexes games by its gameID (string format).

Each gameID has a list of 1 or more messages.

Each message has 3 fields.
- `time`: The time in seconds that the message was sent from the start of the game. Negative time values are messages sent in the pre-game lobby (prior to a match starting).
- `slot`: The id of the player who sent it (local to the game). Is a value from 0-9.
- `text`: The message itself.

## Segments

Given an average annotation time of 6 seconds per message, we've selected the first (roughly) 4200 messages so that we can segment it into 8 sections of 600 messages each (resulting in roughly an hour of annotation per file). `data/segments/data_1.json` and `data/segments/data_2.json` share 10% of the data in common, and `data/segments/data_3.json` and `data/segments/data_4.json` share 5% of the data in common, resulting roughly 3600 unique messages and roughly 600 repeated message instances.

`data/segments/verify.py` was used to verify message counts and duplicate message count.

## Annotator.py

In order to use this annotator tool, please do the following.

1) Make sure to read the annotation guidelines.
2) Copy your `data_x.json` data into `input_data.json`. Do not rename the data, keep it as `input_data.json`.
3) Ensure you have pandas downloaded and installed. `pip install pandas`.
4) Run the file by doing `python annotator.py`.
5) Read through the initial instructions and click Enter.
6) Type a number `0`, `1`, `2`, ... and so on based on they label you want to give the message.

Your progress is saved at the end of ever game. If you quit and come back, you'll start where you left off. If you made a mistake at any point, just make a note of it when providing the data back to us.

## Additional Information

- The raw Kaggle dataset was retrieved on January 31st, 2025, and it the dataset was last updated on Kaggle ~7 years ago (as of February 1st).
- Games that included messages with non-ASCII characters were excluded to attempt to only keep English messages in the data.
- To label a message, it takes roughly 6 seconds.
- Two ChatGPT queries were used in the cleaning of this data, providing assistance with some template code for removing non-English characters. This resulted in 8.64g of C02 emmissions.