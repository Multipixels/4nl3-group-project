
import pandas as pd
from pathlib import Path
import json
import random

# Raw "agreement"

files = [Path("output_for_dota_project_1.json"), Path("output_for_dota_project_2.json"), Path("output_for_dota_project_3.json"), Path("output_for_dota_project_4.json")]
data = []

for my_file in files:
    with open(my_file, "r") as the_data:
        data.append(json.load(the_data))

identical_games_1 = []
identical_games_2 = []

for game in data[1]:
    if game in data[0]:
        identical_games_1.append(game)


for game in data[3]:
    if game in data[2]:
        identical_games_2.append(game)

messages_1 = []
messages_2 = []
messages_3 = []
messages_4 = []
for game in identical_games_1:
    for message in data[0][game]:
        messages_1.append(message["label"])
    for message in data[1][game]:
        messages_2.append(message["label"])

for game in identical_games_2:
    for message in data[2][game]:
        messages_3.append(message["label"])
    for message in data[3][game]:
        messages_4.append(message["label"])

total_messages = len(messages_1) + len(messages_3)
correct = 0

for i in range(len(messages_1)):
    if messages_1[i] == messages_2[i]:
        correct += 1
for i in range(len(messages_3)):
    if messages_3[i] == messages_4[i]:
        correct += 1

p_o = correct/total_messages