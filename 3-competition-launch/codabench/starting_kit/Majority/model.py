import numpy as np
from collections import Counter
import pandas as pd

class Model:
    def __init__(self):
        self.values = {}

    # Train the model
    def fit(self, X, y):
        for game in y:
            for message in game:
                if pd.isna(message): break
                if message["label"] in self.values: self.values[message["label"]] += 1
                else: self.values[message["label"]] = 1
        

    # Predict labels.
    def predict(self, X):
        majority_label = 0
        total = 0
        for key in self.values:
            if self.values[key] > total:
                majority_label = key
                total = self.values[key] 

        predictions = []
        for game in X:
            for message in game:
                if pd.isna(message): break
                predictions.append(majority_label)
        return predictions