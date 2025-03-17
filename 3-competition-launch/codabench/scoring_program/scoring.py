# The scoring program compute scores from:
# - The ground truth
# - The predictions made by the candidate model

# Imports
import json
import os
import matplotlib.pyplot as plt
import io
import base64
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score

# Path
input_dir = '/app/input'    # Input from ingestion program
output_dir = '/app/output/' # To write the scores
reference_dir = os.path.join(input_dir, 'ref')  # Ground truth data
prediction_dir = os.path.join(input_dir, 'res') # Prediction made by the model
score_file = os.path.join(output_dir, 'scores.json')          # Scores
html_file = os.path.join(output_dir, 'detailed_results.html') # Detailed feedback

def write_file(file, content):
    """ Write content in file.
    """
    with open(file, 'a', encoding="utf-8") as f:
        f.write(content)

def get_data():
    """ Get ground truth (y_test) and predictions (y_pred) from the dataset name.
    """
    y_test = pd.read_json(os.path.join(reference_dir, 'test_output.json'))
    y_test = np.array(y_test)
    y_pred = np.genfromtxt(os.path.join(prediction_dir, 'result.predict'))
    return y_test, y_pred

def print_bar():
    """ Display a bar ('----------')
    """
    print('-' * 10)

def main():
    """ The scoring program.
    """
    print_bar()
    print('Scoring program.')
    # Initialized detailed results
    write_file(html_file, '<h1>Detailed results</h1>') # Create the file to give real-time feedback
    scores = 0

    print_bar()
    # Read data
    print('Reading prediction')
    y_test, y_pred = get_data()
    # Compute score
    accuracy = accuracy_score(y_test, y_pred)
    print('Accuracy: {}'.format(accuracy))
    scores = accuracy
    
    # Get duration
    with open(os.path.join(prediction_dir, 'metadata.json')) as f:
        duration = json.load(f).get('duration', -1)

    scores['duration'] = duration

    # Write scores
    print_bar()
    print('Scoring program finished. Writing scores.')
    print(scores)

    write_file(score_file, json.dumps(scores))

if __name__ == '__main__':
    main()
