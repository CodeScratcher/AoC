import re
regex = re.compile(r"move (\d+) from (\d+) to (\d+)")

size_of_stack = 0 

def parse_boxes(boxes):
    global size_of_stack
    tmp = boxes
    guide = tmp.pop()
    parsed = []
    for i in tmp:
        parsed.append([])
        for j in range(0, len(i)):
            if guide[j] != " ":
                parsed[-1].append(i[j])
                if int(guide[j]) > size_of_stack:
                    size_of_stack = int(guide[j])
    return parsed

def get_box_at_layer(boxes, instruction, layer):
    print("GETTING! Layer: " + str(layer) + " Instruction: " + str(instruction))
    #print(boxes[layer])
    box = boxes[layer][instruction - 1]
    if box == " ":
        return get_box_at_layer(boxes, instruction, layer + 1)
    else:
        boxes[layer][instruction - 1] = " "
        return (box, boxes)

def move_box_to_layer(boxes, box, instruction, layer):
    print("MOVING! Layer: " + str(layer) + " Instruction: " + str(instruction))
    if boxes[layer][instruction - 1] != " ":
        boxes.insert(0, [" "] * size_of_stack) 
        boxes[layer][instruction - 1] = box
        # print(boxes[layer])
        return boxes
    if layer == len(boxes) - 1:
        boxes[layer][instruction - 1] = box
        return boxes
    test_box = boxes[layer + 1][instruction - 1]
    if test_box != " ":
        boxes[layer][instruction - 1] = box
        return boxes
    else:
        return move_box_to_layer(boxes, box, instruction, layer + 1)
        
def follow_instruction(boxes, instruction):
    new_boxes = []
    i = 0

    while i < instruction[0]:
        (box, boxes) = get_box_at_layer(boxes, instruction[1], 0)
        new_boxes.append(box)
        i += 1

    new_boxes.reverse()
    
    for x in new_boxes:
        boxes = move_box_to_layer(boxes, x, instruction[2], 0)
    
    return boxes

def follow_instructions(boxes, instructions):
    for k in instructions:
        print(k)
        boxes = follow_instruction(boxes, k)
    return boxes
    
file = open("input", "r")
input = file.read()

x = input.split("\n\n")
boxes = x[0]
instructions = x[1]

boxes = parse_boxes(boxes.split("\n"))
instructions = regex.findall(instructions)
instructions = list(map(lambda x: (int(x[0]), int(x[1]), int(x[2])), instructions))

boxes = follow_instructions(boxes, instructions)

for i in boxes:
    print(i)