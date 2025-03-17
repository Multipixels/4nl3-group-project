# This is a sample code submission.
# It is a simple machine learning classifier.

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
        return np.random.choice(self.labels, size=X.shape[0])