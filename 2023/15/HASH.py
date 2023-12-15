import sys
from functools import reduce

def HASH(str):
    return reduce(lambda acc, c: ((acc + c) * 17) % 256, map(ord, str), 0)


class Lense:
    label: str
    length: int | None

    def __init__(self, label, length):
        self.label = label
        self.length = length

    def __eq__(self, other):
        return self.label == other.label

def log_boxes(boxes):
    for i, b in enumerate(boxes[:4]):
        if len(b) > 0:
            print('Box', i, end=': ')
        for l in b:
            print(f'[{l.label} {l.length}]', end=' ')
        if len(b) > 0:
            print()
    print()


def power(boxes):
    return sum((i+1) * (j+1) * l.length for i, b in enumerate(boxes) for j, l in enumerate(b))

    
if __name__ == '__main__':
    # part 1
    data = sys.stdin.readline().strip().split(',')

    boxes = [list() for _ in range(256)]
    
    for d in data:
        i = len(d) - 1
        length = None
        if d[i].isdecimal():
            length = int(d[i])
            i -= 1
        inst = d[i]
        label = d[:i]
        box = HASH(label)
        print(f'After "{label}{inst}{length}":')
        l = Lense(label, length)

        if inst == '-':
            if l in boxes[box]:
                boxes[box].remove(l)
        
        elif inst == '=':
            if l in boxes[box]:
                i = boxes[box].index(l)
                boxes[box][i].length = length
            else:
                boxes[box].append(l)

        log_boxes(boxes)

    print("Part 1:", sum(map(HASH, data)))
    print("Part 2:", power(boxes))






