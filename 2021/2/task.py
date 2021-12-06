#Part one
with open("input") as f:
    horizontal, depth, aim = 0, 0, 0
    for line in f:
        command, value = line.split()
        if command == "forward":
            horizontal += int(value)
        if command == "down":
            depth += int(value)
        if command == "up":
            depth -= int(value)
    print(horizontal * depth)

#Part two
with open("input") as f:
    horizontal, depth, aim = 0, 0, 0
    for line in f:
        command, value = line.split()
        if command == "forward":
            horizontal += int(value)
            depth += int(value) * aim
        if command == "down":
            aim += int(value)
        if command == "up":
            aim -= int(value)
    print(horizontal * depth)
