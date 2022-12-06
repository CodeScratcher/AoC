def process_elf(elf):
    items = list(map(int, elf.split("\n")))
    return sum(items)

file = open("input", "r")
input = file.read()

elves = input.split("\n\n")
elves = list(map(process_elf, elves))

print("Puzzle 1 solution: " + str(max(elves)))

elves.sort(reverse=True)

print("Puzzle 2 solution: " + str(elves[0] + elves[1] + elves[2]))