
import pandas as pd
from pathlib import Path
import json
import random

data = {}
with open(Path("ground_truth.json"), "r") as the_data:
    data = json.load(the_data)

import matplotlib.pyplot as plt
import numpy as np

categories = ["Positive","Casual","Cooperative" ,"Negative Attitude","Hate Speech / Offensive Language","Verbal Abuse","Miscellaneous","Not English"]
counts = [0, 0, 0, 0, 0, 0, 0, 0] 

for game in data:
    for message in data[game]:
        counts[int(message["label"])] += 1

plt.barh(categories, counts)
plt.title('Message Frequency by Category')
plt.xlabel('Count')
plt.ylabel('Category')
plt.show()