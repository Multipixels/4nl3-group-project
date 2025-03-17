# This is a sample code submission.
# It is a simple machine learning classifier.

import numpy as np

class Model:
    def __init__(self):
        self.labels = []
    
    # Train the model
    def fit(self, X, y):
        for game in y:
            for message in y[game]:
                if y[game][message]["label"] not in self.labels:
                    self.labels.append(y[game][message]["label"])

    # Predict labels.
    def predict(self, X):
        return np.random.choice(self.labels, size=X.shape[0])