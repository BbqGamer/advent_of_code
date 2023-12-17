import sys
import heapq


if __name__ == "__main__":
    grid = [list(map(int, list(line.strip())))
            for line in sys.stdin.readlines()]

    horizontal = [[float('inf')] * len(grid[j]) for j in range(len(grid))]
    vertical = [[float('inf')] * len(grid[j]) for j in range(len(grid))]
    horizontal[0][0] = 0
    vertical[0][0] = 0
    heap = [(0, ((0, 0), 0)), (0, ((0, 0), 1))]
    while len(heap) > 0:
        dist, ((x, y), axis) = heapq.heappop(heap)
        dx, dy = (1, 0) if axis == 0 else (0, 1)

        dists = vertical if axis == 0 else horizontal
        new_dists = {
            1: dist,
            -1: dist
        }
        for i in range(1, 11):
            for j in [1, -1]:
                nx, ny = x + dx * i * j, y + dy * i * j
                if nx < 0 or nx >= len(grid[0]) or ny < 0 or ny >= len(grid):
                    continue
                new_dists[j] += grid[ny][nx]
                if i < 4:
                    continue
                if new_dists[j] < dists[ny][nx]:
                    dists[ny][nx] = new_dists[j]
                    new = (new_dists[j], ((nx, ny), 1 - axis))
                    heapq.heappush(heap, new)
    print("Part 2:", min(horizontal[-1][-1], vertical[-1][-1]))
