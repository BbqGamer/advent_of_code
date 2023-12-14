import sys
from copy import deepcopy
import itertools
import logging


class Platform:

    def __init__(self, input: list[str]):
        self.grid = [list(line.strip()) for line in input]

    def iter_rounded(self, backwards=False):
        I, J = range(len(self.grid)), range(len(self.grid[0]))
        if backwards:
            I = reversed(I)
            J = reversed(J)
        for i, j in itertools.product(I, J):
            if self.grid[i][j] == 'O':
                yield i, j

    def move_rock(self, i, j, di, dj):
        if di == 1:
            self.move_rock_down(i, j)
        elif di == -1:
            self.move_rock_up(i, j)
        elif dj == 1:
            self.move_rock_right(i, j)
        elif dj == -1:
            self.move_rock_left(i, j)

    def move_rock_up(self, i, j):
        while i > 0 and self.grid[i-1][j] == '.':
            self.grid[i][j] = '.'
            self.grid[i-1][j] = 'O'
            i -= 1

    def move_rock_left(self, i, j):
        while j > 0 and self.grid[i][j-1] == '.':
            self.grid[i][j] = '.'
            self.grid[i][j-1] = 'O'
            j -= 1

    def move_rock_right(self, i, j):
        while j < len(self.grid[0]) - 1 and self.grid[i][j+1] == '.':
            self.grid[i][j] = '.'
            self.grid[i][j+1] = 'O'
            j += 1

    def move_rock_down(self, i, j):
        while i < len(self.grid) - 1 and self.grid[i+1][j] == '.':
            self.grid[i][j] = '.'
            self.grid[i+1][j] = 'O'
            i += 1

    def __hash__(self):
        return hash(self.__str__())

    def total_load(self):
        return sum(len(self.grid) - i for i, _ in self.iter_rounded())

    def __str__(self):
        return '\n'.join(''.join(row) for row in self.grid)


if __name__ == "__main__":
    p = Platform(sys.stdin.readlines())

    moved_p = deepcopy(p)
    for i, j in p.iter_rounded():
        moved_p.move_rock_up(i, j)
    print("Part 1:", moved_p.total_load())

    PART2_ITERS = 1000000000
    moved_p = deepcopy(p)
    imap = {hash(moved_p): 0}
    pmap = {0: moved_p}
    for iteration in range(1, PART2_ITERS):
        for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            backwards = False
            if di == 1 or dj == 1:
                backwards = True
            for i, j in moved_p.iter_rounded(backwards):
                moved_p.move_rock(i, j, di, dj)

        if hash(moved_p) in imap:
            start = imap[hash(moved_p)]
            end = iteration
            cycle_length = end - start
            endp = (PART2_ITERS - start) % cycle_length + start
            print("Part 2:", pmap[endp].total_load())
            break

        imap[hash(moved_p)] = iteration
        pmap[iteration] = deepcopy(moved_p)
