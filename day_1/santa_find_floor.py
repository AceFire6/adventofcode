def find_floor(instruction):
    up = instruction.count('(')
    down = instruction.count(')')

    return up - down
