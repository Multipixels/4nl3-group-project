# README - Data

> **This document deals with the categorization of toxic content and messages found online that contain profane, vulgar, or offensive content. Proceed with caution.**

## Raw Data

Data Source: <https://www.kaggle.com/datasets/romovpa/gosuai-dota-2-game-chats> 

To access the data source, you can download it from the link above or use the command below:

`curl -L gosuai-dota-2-game-chats.zip https://www.kaggle.com/api/v1/datasets/download/romovpa/gosuai-dota-2-game-chats`

## Cleaned Data

We used `filter.text.py` to produce `filtered_output_1.csv`, which filters out any game that has non-English characters (in hopes of removing messages in other languages, like Russian).

We then used `relabel_matches.py` to produce `filtered_output_2.json` to relabel the match id's from arbitrary integers to 0, 1, 2, ..., n. We also only kept the first 100k rows of data, and turned it from `csv` to `json` format.

Finally, `final_data.json` is the same as `filtered_output_2.json` except we manually removed the last game, in case it was cut off short when we said that we kept the first 100k rows of data in the first stop.

## Segments

Given an average annotation time of 6 seconds per message, we've selected the first (roughly) 4200 messages so that we can segment it into 8 sections of 600 messages each (resulting in roughly an hour of annotation per file). `data/segments/data_1.json` and `data/segments/data_2.json` share 10% of the data in common, and `data/segments/data_3l.sjon` and `data/segments/data_4.json` share 5% of the data in common, resulting roughly 3600 unique messages and roughly 600 repeated message instances.

`data/segments/verify.py` was used to verify message counts and duplicate message count.

## How to use the Data

`final_data.json` is a collection of chatlogs from 5151 games of Dota 2. These games are indexed from 0-5150, where each game consists of 0 or more messages. Each message has the following attributes:

- `time`: The time (in seconds) that the message was sent relative to the start of the game. Messages that have a negative `time` value are messages that were sent in the pre-game lobby.
- `slot`: A match-specific user id of the player who sent the message. `slot` ranges from 0-9, where players 0-4 are on one team, and 5-9 are on the other team.
- `text`: The message itself.

## Annotator.py

In order to use this annotator tool, please do the following.

1) Make sure to read the annotation guidelines.
2) Copy your `data_x.json` data into `input_data.json`. Do not rename the data, keep it as `input_data.json`.
3) Ensure you have pandas downloaded and installed. `pip install pandas`.
4) Run the file by doing `python annotator.py`.
5) Read through the initial instructions and click Enter.
6) Type a number `0`, `1`, `2`, ... and so on based on they label you want to give the message.
7) Your progress is saved at the end of ever game. If you quit and come back, you'll start where you left off. If you made a mistake at any point, just make a note of it when providing the data back to us.

## Additional Information

- The raw Kaggle dataset was retrieved on January 31st, 2025, and it the dataset was last updated on Kaggle ~7 years ago (as of February 1st).
- Games that included messages with non-ASCII characters were excluded to attempt to only keep English messages in the data.
- To label a message, it takes roughly 6 seconds.