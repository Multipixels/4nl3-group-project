import numpy as np
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

class Model:
    def __init__(self):
        self.lr_model = LogisticRegression()
        self.vectorizer = TfidfVectorizer()

    def vectorize_train_data(self, X):
        X_vect = self.vectorizer.fit_transform(X)
        return X_vect

    def vectorize_test_data(self, X):
        data = []
        for game in X:
            for message in game:
                if pd.isna(message): break
                data.append(message["text"])

        X_vect = self.vectorizer.transform(data)
        return X_vect

    # Train the model
    def fit(self, X, y):
        data = []
        label = []
        for game in X:
            for message in game:
                if pd.isna(message): break
                data.append(message["text"])

        for game in y:
            for message in game:
                if pd.isna(message): break
                label.append(message["label"])

        X_vect = self.vectorize_train_data(data)
        self.lr_model.fit(X_vect, label)        

    # Predict labels.
    def predict(self, X):
        X_vect = self.vectorize_test_data(X)
        y_pred = self.lr_model.predict(X_vect)
        return y_pred