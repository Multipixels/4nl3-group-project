# This is a sample code submission.
# It is a simple machine learning classifier.

import numpy as np

class Model:
    def __init__(self):
        pass
    
    # Train the model
    def fit(self, X, y):
        self.labels = np.unique(y)

    # Predict labels.
    def predict(self, X):
        return np.random.choice(self.labels, size=X.shape[0])