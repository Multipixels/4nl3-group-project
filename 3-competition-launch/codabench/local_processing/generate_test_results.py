# The ingestion program is the program that:
# 1. Take participant's code submission
# 2. Train the given model on the training data
# 3. Make predictions on the test data, and save them to forward them to the scoring program

# Imports
import json
import os
import sys
import time
import numpy as np
import pandas as pd

def get_data():
    """ Get X_train, y_train and X_test from the dataset name.
    """
    # Read data
    X_train = pd.read_json("train_input.json", orient="index")
    y_train = pd.read_json('train_output.json', orient="index")
    X_test = pd.read_json("test_input.json", orient="index")

    # Convert to numpy arrays
    X_train, y_train, X_test = np.array(X_train), np.array(y_train), np.array(X_test)
    return X_train, y_train, X_test

def print_bar():
    """ Display a bar ('----------')
    """
    print('-' * 10)

def main():
    """ The ingestion program.
    """
    print_bar()
    print('Ingestion program.')
    from model import Model # The model submitted by the participant
    start = time.time()

    print_bar()
    # Read data
    print('Reading data')
    X_train, y_train, X_test = get_data()
    # Initialize model
    print('Initializing the model')
    m = Model()
    # Train model
    print('Training the model')
    m.fit(X_train, y_train)
    # Make predictions
    print('Making predictions')
    y_pred = m.predict(X_test)
    # Save predictions
    np.savetxt('submit_these_result.predict', y_pred, fmt='%s')

    # End
    print('Ingestion program finished.')
    print_bar()

if __name__ == '__main__':
    main()
