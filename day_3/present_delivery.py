X_POS = 0
Y_POS = 0

def go_up():
    global Y_POS
    Y_POS += 1

def go_down():
    global Y_POS
    Y_POS -= 1

def go_right():
    global X_POS
    X_POS += 1

def go_left():
    global X_POS
    X_POS -= 1

def count_house_visits(elf_directions):
    global X_POS, Y_POS
    directions = {
        '^': go_up,
        'v': go_down,
        '>': go_right,
        '<': go_left,        
    }
    total_houses_visited = 0
    for elf_direction in elf_directions.split('\n'):
        # Starting point 0, 0
        houses = {
            0: [0,]
        }

        for i in elf_direction:
            directions[i]()
            if not houses.get(Y_POS):
                houses[Y_POS] = []
            if not X_POS in houses[Y_POS]:
                houses[Y_POS].append(X_POS)
                
        for i in houses:
            total_houses_visited += len(set(houses[i]))
    return total_houses_visited
        
