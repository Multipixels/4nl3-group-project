import os
import json
import numpy as np
import pandas as pd
from collections import Counter
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

import MajorityExample
import RandomExample

input_dir = "../data/"

def get_data():
    """Load the ground truth data from the JSON file located in ../data/ground_truth.json."""
    X_train = pd.read_csv(os.path.join(input_dir, 'train_input.json'))
    y_train = pd.read_csv(os.path.join(input_dir, 'train_output.json'))
    X_test = pd.read_csv(os.path.join(input_dir, 'test_input.json'))

    return X_train, y_train, X_test


def vectorize_data(X_train, X_test):
    """Vectorize text data using TF-IDF."""
    vectorizer = TfidfVectorizer()
    X_train_vect = vectorizer.fit_transform(X_train)
    X_test_vect = vectorizer.transform(X_test)
    return X_train_vect, X_test_vect, vectorizer


def evaluate_baselines(X_train_vect, X_test_vect, y_train, y_test):
    """Evaluate baseline classifiers and return their accuracies."""
    majority_model = MajorityExample.Model()
    majority_model.fit(X_train_vect, y_train)
    y_pred_majority = majority_model.predict(X_test_vect)
    accuracy_majority = accuracy_score(y_test, y_pred_majority)

    random_model = RandomExample.Model()
    random_model.fit(X_train_vect, y_train)
    y_pred_random = random_model.predict(X_test_vect)
    accuracy_random = accuracy_score(y_test, y_pred_random)

    return accuracy_majority, accuracy_random


def train_logistic_regression(X_train_vect, X_test_vect, y_train, y_test):
    """Train a Logistic Regression model and return its accuracy."""
    lr_model = LogisticRegression()
    lr_model.fit(X_train_vect, y_train)
    y_pred_lr = lr_model.predict(X_test_vect)
    accuracy_lr = accuracy_score(y_test, y_pred_lr)
    return accuracy_lr


def main():
    X_train, y_train, X_test = get_data()
    X_train_vect, X_test_vect, _ = vectorize_data(X_train, X_test)
    X_train_vect, X_test_vect, _ = vectorize_data(y_train, X_test)

    accuracy_majority, accuracy_random = evaluate_baselines(X_train_vect, X_test_vect, y_train, y_test)
    
    print("Majority Baseline Accuracy:", accuracy_majority)
    print("Random Baseline Accuracy:", accuracy_random)

    accuracy_lr = train_logistic_regression(
        X_train_vect, X_test_vect, y_train, y_test)
    print("Logistic Regression Accuracy:", accuracy_lr)


if __name__ == "__main__":
    main()
