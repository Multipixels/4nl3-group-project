# Getting the Data

To download the raw data directly from the source, either

1) Go to <https://www.kaggle.com/datasets/romovpa/gosuai-dota-2-game-chats> and download with a Kaggle account
2) Run `curl -L gosuai-dota-2-game-chats.zip https://www.kaggle.com/api/v1/datasets/download/romovpa/gosuai-dota-2-game-chats`.

Extract the CSV and rename it to raw_data.csv. Save it in this directory. The .gitignore ensures it's not committed (it can't be, it's too big).