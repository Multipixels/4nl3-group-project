import numpy as np
from collections import Counter
import pandas as pd

class Model:
    def __init__(self):
        values = {}

    # Train the model
    def fit(self, X, y):
        values = {}
        for game in y:
            for message in y[game]:
                if pd.isna(message): break
                if message["label"] in values: values[message["label"]] += 1
                else: values[message["label"]] = 1
        

    # Predict labels.
    def predict(self, X):
        predictions = []
        for game in X:
            for message in game:
                if pd.isna(message): break
                predictions.append(self.majority_label)
        return predictions