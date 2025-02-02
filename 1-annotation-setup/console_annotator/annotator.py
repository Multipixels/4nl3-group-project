
import pandas as pd
from pathlib import Path
import json
import random

instructions = \
"""
Thank you for participating in our annotation task!
Make sure to read the annotation guidelines document provided before proceeding.
This task requires you to identify the label to apply to the message with only the context provided.

The labels are:
    Positive - compliments, good sportmanship, etc.
    Casual - messages non-related/off-topic to the game 
    Cooperative - neutral messages on-topic about the game
    Negative Attitude - giving up, attempting to help the other team/hurt their own team
    Hate Speech/Offensive Language - hateful messages towards individuals/groups related to their sexuality, religion, gender, etc.
    Verbal Abuse - generally hateful messages that don't fall under the above category
    Miscellaneous - anything that doesn't fall into the above categories
    
You will have an additional option to mark a game as having non-English messages, which will swap out the current
game context with another one from the backup. Do not use this for messages that contain random gibberish.
"""

labels = ["Positive", "Casual", "Cooperative", "Negative Attitude", "Hate Speech/Offensive Language", "Verbal Abuse", "Miscellaneous", "Not English."]

data_col = "text"

delimiter = "="*60

names = ["Alice", "Bob", "Chad", "Dave", "Eve", 
         "Frank", "Grace", "Hettie", "Ivan", "Judy", 
         "Kyle", "Laurel", "Michael", "Niaj", "Oscar", 
         "Peggy", "Quinn", "Rupert", "Sybil", "Ted", 
         "Ursula", "Victor", "Walt", "Xavier", "Yanny", 
         "Zoe"]


def getPlayerMessage(game, nameIds, messageNumber):
    seconds = (int(game[messageNumber]['time'] % 60))
    if int(game[messageNumber]['time'])< 0:
        seconds = 60 - seconds
    time = f"{int(game[messageNumber]['time']//60):1}:{seconds:02}"
    player = game[messageNumber]['slot']
    text = game[messageNumber]['text']

    return f"[{time}] {names[nameIds[player]]}: {text}"

def main():
    # Read my data file
    with open('input_data.json') as data:
        my_data = json.load(data)

    # Make sure I don't overwrite anything!
    startingGameId = 0
    my_file = Path("output_for_dota_project.json")
    if my_file.is_file():
        with open(my_file, "r") as the_data:
            the_json_data = json.load(the_data)
            for game in the_json_data:
                startingGameId = max(startingGameId, int(game)+1)

    print(instructions)

    input("Press ENTER when you are ready to proceed.")
    print()

    # Loop over data and request labels
    all_data = {}
    for game in my_data:
        if(int(game) < startingGameId):
            continue

        game_data = []
        last_message_time = my_data[game][-1]['time']
        last_message_time_string = f"{(int(last_message_time)//60):1}:{int(last_message_time)%60:02}"

        for i in range(len(my_data[game])):
            message_data = {}
            print(delimiter)
            print(f"Game {game} - Message ({i+1}/{len(my_data[game])}) - Last Message Time: {last_message_time_string}")
            random.seed(game)
            nameIds = []
            for j in range(10):
                a = random.randint(0,25)
                while a in nameIds:
                    a = random.randint(0,25)
                nameIds.append(a)

            for j in range(i-5,i+5):
                if j < 0: print(); continue
                if j >= len(my_data[game]): print(); continue
                if j == i: print("--> ", end="") 
                else: print("    ", end="")
                print(getPlayerMessage(my_data[game], nameIds, j))

            print()
            print(" ".join(["(" + str(i) + ") " + str(k) for i,k in enumerate(labels)]))
                
            label = input("Your label: ") 
            while(label not in ["0", "1", "2", "3", "4", "5", "6", "7"]):
                label = input("Please enter a valid label from 0 to 7: ")
            
            message_data["time"] = my_data[game][i]["time"]
            message_data["slot"] = my_data[game][i]["slot"]
            message_data["text"] = my_data[game][i]["text"]
            message_data["label"] = label
            game_data.append(message_data)

            print(); print(); print(); print(); print(); print(); print(); print(); print(); print(); print(); print()

        all_data[str(game)] = game_data
        # Saving
        if(my_file.is_file()):
            with open(my_file, "r") as outfile: 
                data = json.load(outfile)
            all_data = data | all_data
            
        with open(my_file, "w") as outfile: 
            json.dump(all_data, outfile, indent = 4)




if __name__ == '__main__':
    main()
