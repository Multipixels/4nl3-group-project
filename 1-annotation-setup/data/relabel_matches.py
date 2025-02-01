import pandas as pd
import json

def main():
    input_csv = "filtered_output_1.csv"
    df = pd.read_csv(input_csv)

    gameId = -1
    newGameId = -1
    print(df.index)
    counter = 0
    for index, row in df.iterrows():
        if (counter > 100000): break
        if row["match"] != gameId: 
            gameId = row["match"]
            newGameId += 1
        df.at[counter, "match"] = newGameId
        counter += 1
    
    output_json = "filtered_output_2.json"
    json_string = df[0:100000].groupby('match').apply(lambda x: x.to_dict(orient="records"))

    i=0
    for row in json_string:
        for x in row: x.pop("match")
        i+=1

    json_object = json.loads(json_string.to_json())

    out_file = open(output_json, "w")
    json.dump(json_object, out_file, indent=4)
    out_file.close()

if __name__ == "__main__":
    main()
