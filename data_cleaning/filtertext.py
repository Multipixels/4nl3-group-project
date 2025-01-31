import pandas as pd
from langdetect import detect
from tqdm import tqdm


def main():
    input_csv = "filtered_output.csv"
    df = pd.read_csv(input_csv)

    def contains_non_ascii(text):
        # Handle NaN values
        if pd.isna(text):
            return True

        return any(ord(char) > 127 for char in text)

    english_rows = []
    for _, row in tqdm(df.iterrows(), total=len(df), desc="Processing rows"):
        if contains_non_ascii(row['text']):
            continue

        english_rows.append(row)

    english_rows = pd.DataFrame(english_rows)

    output_csv = "filtered_output2.csv"
    english_rows.to_csv(output_csv, index=False)

    print(f"\nFiltered data saved to {output_csv}")
    print(f"Kept {len(english_rows)} English rows")


if __name__ == "__main__":
    main()
