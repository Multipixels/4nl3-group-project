# This is a sample code submission.
# It is a simple machine learning classifier.

import numpy as np
from collections import Counter

class Model:
    def __init__(self):
        values = {}

    # Train the model
    def fit(self, X, y):
        values = {}
        for game in y:
            for message in y[game]:
                    if y[game][message]["label"] in values: values[y[game][message]["label"]] += 1
                    else: values[y[game][message]["label"]] = 1
        

    # Predict labels.
    def predict(self, X):
        return np.full(shape=X.shape[0], fill_value=self.majority_label)