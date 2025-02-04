import json

dicts = []
games = {}
gameIds = []
gameToMessages = {}

# https://stackoverflow.com/questions/952914/how-do-i-make-a-flat-list-out-of-a-list-of-lists
def make_flat_list(list):
    flat_list = [
        x
        for xs in list
        for x in xs
    ]
    return flat_list

for i in range(8):
    with open(f"./data_{i+1}.json") as file:
        content = json.loads(file.read())
        dicts.append(content)

for i in range(8):
    numGames = len(dicts[i])

    for game in dicts[i]:
        if game in games:
            games[game] += 1
        else: games[game] = 1
        if game not in gameToMessages:
            gameToMessages[game] = len(dicts[i][game])
        gameIds.append(game)

    messages = make_flat_list(dicts[i].values())
    numMessages = len([j["text"] for j in messages])

    print(f"data_{i+1}.json has {numGames} games and {numMessages} messages")

print(games)
sortedGameIds = sorted([int(hehe) for hehe in games])
print(sortedGameIds)
for i in range(sortedGameIds[-1]):
    if i not in sortedGameIds: print(i)

duplicates = 0
for j in games:
    if games[j] >= 2:
        duplicates += gameToMessages[str(j)]

print(duplicates)