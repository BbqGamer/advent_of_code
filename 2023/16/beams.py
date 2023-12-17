import sys

I = complex(0, 1)

def get_dirs(cur_dir, symbol):
    if symbol == '|':
        if abs(cur_dir.real) == 1.0:
            return [cur_dir * I, cur_dir * -I]
        else:
            return [cur_dir]
    elif symbol == '-':
        if abs(cur_dir.imag) == 1.0:
            return [cur_dir * I, cur_dir * -I]
        else:
            return [cur_dir]
    elif symbol == '/':
        if abs(cur_dir.real) == 1.0:
            return [cur_dir * -I]
        else:
            return [cur_dir * I]
    elif symbol == '\\':
        if abs(cur_dir.imag) == 1.0:
            return [cur_dir * -I]
        else:
            return [cur_dir * I]
    else:
        raise ValueError(f"{symbol}: is not supported")


def draw_G(grid, G):
    new_grid = [['.' for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for (cur, dir), end in G.items():
        new_grid[int(cur.imag)][int(cur.real)] = '#'
        while cur != end:
            cur += dir
            new_grid[int(cur.imag)][int(cur.real)] = '#'
    return ["".join(row) for row in new_grid]
        

def energize(i_pos, i_dir):
    print(i_pos, i_dir)
    pos = i_pos 
    dir = i_dir
    G = dict()
    stack = [(pos, dir)]
    while len(stack) > 0:
        start = stack.pop()
        if start in G:
            continue
        cur, dir = start
        cur = cur + dir
        if int(cur.real) < 0 or int(cur.real) >= len(grid[0]) or \
           int(cur.imag) < 0 or int(cur.imag) >= len(grid):
                continue
        symbol = grid[int(cur.imag)][int(cur.real)]
        can_add = True
        while symbol == '.':
            cur += dir
            if int(cur.real) < 0 or int(cur.real) >= len(grid[0]) or \
               int(cur.imag) < 0 or int(cur.imag) >= len(grid):
                    can_add = False
                    cur -= dir
                    break
            symbol = grid[int(cur.imag)][int(cur.real)]
         
        G[start] = cur
        if can_add:
            stack.extend([(cur, d) for d in get_dirs(dir, symbol)])

    # This is a workaround that in my imput 0, 0 was already a mirror
    first = G[(i_pos, i_dir)]
    del G[(i_pos, i_dir)]
    G[(i_pos + i_dir, i_dir)] = first
    drawn = draw_G(grid, G)
    return sum(row.count("#") for row in drawn)

if __name__ == "__main__":
    grid = [l.strip() for l in sys.stdin.readlines()]
    print("Part 1: ", energize(complex(-1, 0), complex(1, 0)))

    scores = []
    for i in range(len(grid)):
        scores.append(energize(complex(-1, i), complex(1, 0)))
        scores.append(energize(complex(len(grid[0]), i), complex(-1, 0)))
    for j in range(len(grid[0])):
        scores.append(energize(complex(j, -1), complex(0, 1)))
        scores.append(energize(complex(j, len(grid)), complex(0, -1)))
    print("Part 2: ", max(scores))
        






