from sys import stdin
import numpy as np

moves = {
    "R": np.array([1,0]),
    "U": np.array([0,1]),
    "L": np.array([-1,0]),
    "D": np.array([0,-1])
}

def flat(v):
    return np.array(
        [np.sign(v[0]),
         np.sign(v[1])])


            
def simulateKnots(instructions, num_knots):
    knots = [np.array([0,0]) for x in range(num_knots)]

    visited = set()
    visited.add(tuple(knots[0]))

    for move, steps in instructions:
        for i in range(int(steps)):
            #move step by step, start with Head
            knots[0] += moves[move]
            
            #the rest of the knots
            for k in range(1,num_knots):
                head = knots[k-1]
                tail = knots[k]
                delta = head - tail

                if(any([abs(x) == 2 for x in delta])):
                    knots[k] += flat(delta)
                
                if(k == num_knots-1):
                    visited.add(tuple(knots[k]))

    return len(visited)

            
if __name__ == "__main__":
    instructions = [line.split() for line in stdin]
    print("Part 1: ", simulateKnots(instructions, 2))
    print("Part 2: ", simulateKnots(instructions, 10))
