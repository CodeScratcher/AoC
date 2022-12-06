def get_priority(char): 
    if char.isupper():
        return ord(char) - 64 + 26
    else:
        return ord(char) - 96

def compartment_to_priority(comp):
    return sum(map(get_priority, comp))

def split_list(lst):
    middle_index = int(len(lst) / 2)
    return [lst[:middle_index], lst[middle_index:]]

def filter_dual_compartments(comp):
    answer_list = []
    for x in comp[0]:
        if x in comp[1]:
            answer_list.append(x)
    return answer_list
    
def tri_compartments(comp):
#    print(comp)
    for x in comp[0]:
        if x in comp[1] and x in comp[2]:
            return x
    raise Exception("No badges in compartments")

# Thanks to stack overflow: https://stackoverflow.com/a/312464
def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

file = open("input", "r")
input = file.read()

compartments = input.split("\n")
compartments = list(map(split_list, compartments))

filtered_compartments = map(set, map(filter_dual_compartments, compartments))
compartment_priorities = map(compartment_to_priority, filtered_compartments)

print("Puzzle 1: " + str(sum(compartment_priorities)))

added_compartments =  list(map(set, map(lambda x: x[0] + x[1], compartments)))
groups = chunks(added_compartments, 3)
badges = map(tri_compartments, groups)

print("Puzzle 2: " + str(sum(map(get_priority, badges))))