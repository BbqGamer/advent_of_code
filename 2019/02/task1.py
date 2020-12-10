with open('input.txt', 'r') as f:
    memory=list(map(int, f.read().split(',')))

for i in range(100):
    for j in range(100):                
        position = 0
        program = memory.copy()
        program[1] = i
        program[2] = j
        while(True):
            opt_code = program[position]
            if opt_code == 99:
                if program[0] == 19690720:
                    print(i,j)
                break
            else:
                location = program[position+3]
                input_1 = program[position+1]
                input_2 = program[position+2]
                if opt_code == 1:
                    program[location] = program[input_1] + program[input_2]
                elif opt_code == 2:
                    program[location] = program[input_1] * program[input_2]
                else:
                    print("Unknown opt code", program[position])
                    print(position)
                    exit()
            position += 4
