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

# Paths
input_dir = '/app/input_data/' # Data
output_dir = '/app/output/'    # For the predictions
program_dir = '/app/program'
submission_dir = '/app/ingested_program' # The code submitted
sys.path.append(output_dir)
sys.path.append(program_dir)
sys.path.append(submission_dir)

def get_data():
    """ Get X_train, y_train and X_test from the dataset name.
    """
    # Read data
    X_train = pd.read_json(os.path.join(input_dir,  'train_input.json'), orient="index")
    y_train = pd.read_json(os.path.join(input_dir,  'train_output.json'), orient="index")
    X_test = pd.read_json(os.path.join(input_dir,  'test_input.json'), orient="index")

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
    print('Ingestion program finished. Moving on to scoring')
    print_bar()

if __name__ == '__main__':
    main()
