import json
import numpy as np
import pandas as pd
from collections import Counter
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


class RandomBaselineClassifier:
    """A simple baseline classifier that randomly predicts one of the classes."""

    def fit(self, X, y):
        self.labels = np.unique(y)

    def predict(self, X):
        return np.random.choice(self.labels, size=X.shape[0])


class MajorityBaselineClassifier:
    """A simple baseline classifier that predicts the most common class."""

    def fit(self, X, y):
        self.majority_label = Counter(y).most_common(1)[0][0]

    def predict(self, X):
        return np.full(shape=X.shape[0], fill_value=self.majority_label)


def get_truth_data() -> pd.DataFrame:
    """Load the ground truth data from the JSON file located in ../data/ground_truth.json."""
    data_file = Path("../data/ground_truth.json")
    with open(data_file, "r") as f:
        json_data = json.load(f)

    all_data = []
    for key, records in json_data.items():
        all_data.extend(records)

    df = pd.DataFrame(all_data)
    return df


def split_data(df: pd.DataFrame):
    """Split the DataFrame into training and testing sets."""
    return train_test_split(df["text"], df["label"], test_size=0.3, random_state=42)


def vectorize_data(X_train, X_test):
    """Vectorize text data using TF-IDF."""
    vectorizer = TfidfVectorizer()
    X_train_vect = vectorizer.fit_transform(X_train)
    X_test_vect = vectorizer.transform(X_test)
    return X_train_vect, X_test_vect, vectorizer


def evaluate_baselines(X_train_vect, X_test_vect, y_train, y_test):
    """Evaluate baseline classifiers and return their accuracies."""
    majority_model = MajorityBaselineClassifier()
    majority_model.fit(X_train_vect, y_train)
    y_pred_majority = majority_model.predict(X_test_vect)
    accuracy_majority = accuracy_score(y_test, y_pred_majority)

    random_model = RandomBaselineClassifier()
    random_model.fit(X_train_vect, y_train)
    y_pred_random = random_model.predict(X_test_vect)
    accuracy_random = accuracy_score(y_test, y_pred_random)

    return accuracy_majority, accuracy_random


def train_logistic_regression(X_train_vect, X_test_vect, y_train, y_test):
    """Train a Logistic Regression model and return its accuracy."""
    lr_model = LogisticRegression(max_iter=1000)
    lr_model.fit(X_train_vect, y_train)
    y_pred_lr = lr_model.predict(X_test_vect)
    accuracy_lr = accuracy_score(y_test, y_pred_lr)
    return accuracy_lr


def main():
    df = get_truth_data()
    X_train, X_test, y_train, y_test = split_data(df)
    X_train_vect, X_test_vect, _ = vectorize_data(X_train, X_test)

    accuracy_majority, accuracy_random = evaluate_baselines(
        X_train_vect, X_test_vect, y_train, y_test)
    print("Majority Baseline Accuracy:", accuracy_majority)
    print("Random Baseline Accuracy:", accuracy_random)

    accuracy_lr = train_logistic_regression(
        X_train_vect, X_test_vect, y_train, y_test)
    print("Logistic Regression Accuracy:", accuracy_lr)


if __name__ == "__main__":
    main()
