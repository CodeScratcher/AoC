def split_on(thing):
    return lambda x: x.split(thing)

def to_int_pairs(pair):
    return list(map(int, pair))

def parse_pair(pair):
    elves = pair.split(",")
    elves = map(split_on("-"), elves)
    elves = list(map(to_int_pairs, elves))
    return elves
    
def overlaps(pair):
    parsed_pair = parse_pair(pair)
    left_overlaps_right = (parsed_pair[0][0] <= parsed_pair[1][0] and parsed_pair[0][1] >= parsed_pair[1][0]) or (parsed_pair[0][0] <= parsed_pair[1][1] and parsed_pair[0][1] >= parsed_pair[1][1])
    right_overlaps_left = (parsed_pair[1][0] <= parsed_pair[0][0] and parsed_pair[1][1] >= parsed_pair[0][0]) or (parsed_pair[1][0] <= parsed_pair[0][1] and parsed_pair[1][1] >= parsed_pair[0][1])
    
    return left_overlaps_right or right_overlaps_left

def test_int(x):
    print(int(x))
    return int(x)

file = open("input", "r")
input = file.read()

pairs = input.split("\n")

bools = map(overlaps, pairs)

print("Puzzle 1: " + str(sum(map(int, bools))))