import pandas as pd
import json
from pathlib import Path
from sklearn.model_selection import train_test_split
import numpy as np


def get_truth_data() -> pd.DataFrame:
    """Load the ground truth data from the JSON file located in ../data/ground_truth.json."""
    data_file = Path("../data/ground_truth.json")
    with open(data_file, "r") as f:
        json_data = json.load(f)

    all_data = []
    for key, records in json_data.items():
        for record in records:
            record["conversation_id"] = key
            all_data.append(record)

    df = pd.DataFrame(all_data)
    return df


def split_data(df: pd.DataFrame):
    """Randomly shuffle the DataFrame and split it into training, validation, and testing sets."""
    train, validate, test = np.split(df.sample(frac=1, random_state=42),
                                     [int(.6 * len(df)), int(.8 * len(df))])
    return train, validate, test


def save_split_data(split_df: pd.DataFrame, filepath: str):
    """
    Save a DataFrame to JSON with the format:
        {
            "0": [ list of record dictionaries ]
        }
    """
    records = split_df.to_dict(orient="records")
    json_output = {"0": records}

    with open(filepath, "w") as f:
        json.dump(json_output, f, indent=4)


def main():
    df = get_truth_data()
    train, validate, test = split_data(df)
    save_split_data(train, r'../data/train.json')
    save_split_data(validate, r'../data/validate.json')
    save_split_data(test, r'../data/test.json')
    print("Data split and stored in data folder")


if __name__ == "__main__":
    main()
