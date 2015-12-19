def find_basement_instruction(instruction_list):
    current_floor = 0
    position = 0
    for instruction in instruction_list:
        position += 1
        current_floor += (-1 if instruction == ')' else 1)
        if current_floor == -1:
            return position
    return -1
