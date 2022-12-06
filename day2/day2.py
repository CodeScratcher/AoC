def get_won_score(pair):
    won = False
    
    match pair[0]:
        case "A": # ROCK
            won = pair[1] == "Y"
        case "B": # PAPER
            won = pair[1] == "Z"
        case "C": # SCISSORS
            won = pair[1] == "X"
    return int(won) * 2

def score_for_two(pair):
    CONVERTER = {
        "X": {
            "A": "Z",
            "B": "X",
            "C": "Y"
        },
        "Y": {
            "A": "X",
            "B": "Y",
            "C": "Z"
        },
        "Z": {
            "A": "Y",
            "B": "Z",
            "C": "X"
        }
    }
    
    true_pair = [pair[0], CONVERTER[pair[1]][pair[0]]]
    return score(true_pair)

def score(pair):
    CONVERSION = {
        "X": "A",
        "Y": "B",
        "Z": "C"
    }
    SCORE_CHART = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }
    
    won_score = 0
    if pair[0] == CONVERSION[pair[1]]:
        won_score = 1
    else:
        won_score = get_won_score(pair)
    
    return won_score * 3 + SCORE_CHART[pair[1]]

file = open("input", "r")

input = file.read()

guide = input.split("\n")
guide = list(map(lambda x: x.split(" "), guide))

scores = list(map(score, guide))

print("Puzzle 1: " + str(sum(scores)))

true_scores = list(map(score_for_two, guide))

print("Puzzle 2: " + str(sum(true_scores)))