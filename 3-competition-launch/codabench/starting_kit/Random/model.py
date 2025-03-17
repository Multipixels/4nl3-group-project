import numpy as np
import pandas as pd

class Model:
    def __init__(self):
        self.labels = []
    
    # Train the model
    def fit(self, X, y):
        for game in y:
            for message in game:
                if pd.isna(message): break
                if message["label"] not in self.labels:
                    self.labels.append(message["label"])

    # Predict labels.
    def predict(self, X):
        predictions = []
        for game in X:
            for message in game:
                if pd.isna(message): break
                predictions.append(np.random.choice(self.labels))
        return predictions