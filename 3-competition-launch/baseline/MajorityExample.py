# This is a sample code submission.
# It is a simple machine learning classifier.

import numpy as np
from collections import Counter

class Model:
    def __init__(self):
        pass

    # Train the model
    def fit(self, X, y):
        self.majority_label = Counter(y).most_common(1)[0][0]

    # Predict labels.
    def predict(self, X):
        return np.full(shape=X.shape[0], fill_value=self.majority_label)