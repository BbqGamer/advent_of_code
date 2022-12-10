from sys import stdin

WIDTH = 40
HEIGHT = 6
screen = [[" " for i in range(WIDTH)] for i in range(HEIGHT)]

data = [instr for instr in stdin.read().splitlines()]

cycle = 0
cycles_to_check = range(20,221,40)
X = 1
values = []

def process_cycle(cycle, X):
    x_pos = (cycle-1) % WIDTH
    y_pos = (cycle-1) // WIDTH
    if x_pos in [X-1, X, X+1]:
        screen[y_pos][x_pos] = "#"
    else:
        screen[y_pos][x_pos] = "."
 

for inst in data:
    a = inst.split()
    if len(a) == 1:
        cycle += 1
        process_cycle(cycle, X)
        # noop
        if cycle in cycles_to_check:
            values.append(cycle * X)
            # check

    else:
        for i in range(2):
            cycle += 1
            process_cycle(cycle, X)
            if cycle in cycles_to_check:
                values.append(cycle * X)
                # check
        X += int(a[1])
        # add


print("Part 1: ", sum(values))

#print screen
print("Part 2: ")
for line in screen:
    print(*line, sep="")