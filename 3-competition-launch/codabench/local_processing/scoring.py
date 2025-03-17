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
import ingestion

def write_file(file, content):
    """ Write content in file.
    """
    with open(file, 'a', encoding="utf-8") as f:
        f.write(content)

def get_data():
    """ Get ground truth (y_test) and predictions (y_pred) from the dataset name.
    """
    y_test = pd.read_json('validate_output.json', orient="index")
    y_test = np.array(y_test)
    y_pred = np.genfromtxt('result.predict')

    y_real_test = []
    for game in y_test:
        for message in game:
            if pd.isna(message): break
            y_real_test.append(int(message["label"]))

    return y_real_test, y_pred

def print_bar():
    """ Display a bar ('----------')
    """
    print('-' * 10)

def main():
    ingestion.main()

    """ The scoring program.
    """
    print_bar()
    print('Scoring program.')
    # Initialized detailed results
    # write_file(html_file, '<h1>Detailed results</h1>') # Create the file to give real-time feedback
    scores = {}

    print_bar()
    # Read data
    print('Reading prediction')
    y_test, y_pred = get_data()
    # Compute score
    print(y_test)
    print(y_pred)
    accuracy = accuracy_score(y_test, y_pred)
    print('Accuracy: {}'.format(accuracy))
    scores["accuracy"] = accuracy
    
    # Compute false positives
    false_positive_count = 0
    should_not_report_count = 0
    for i in range(len(y_pred)):
        if y_pred[i] in [3, 4, 5] and y_test[i] not in [3, 4, 5]:
            false_positive_count += 1
        if y_test[i] not in [3,4,5]:
            should_not_report_count += 1

    scores['false_report_rate'] = false_positive_count / should_not_report_count
    
    # Get duration
    with open('metadata.json') as f:
        duration = json.load(f).get('duration', -1)

    scores['duration'] = duration

    # Write scores
    print_bar()
    print('Scoring program finished. Writing scores.')
    print(scores)

    write_file("score.json", json.dumps(scores))

if __name__ == '__main__':
    main()
