
import sys
sys.stdin = open('input.txt')


def gridChallenge(grid):
    # Write your code here
    glist = [[] for _ in range(len(grid))]
    print(glist)
    # i = 0
    for idx in range(len(grid)):
        for a in grid[idx]:
            glist[idx].append(a)
        glist[idx].sort()
    print(glist)

    zgrid = zip(*glist)
    for g in zgrid:
        inita = g[0]
        for a in g[1:]:
            # print(g, a)
            if a >= inita:
                inita = a
            else:
                inita = a
                return 'NO'

    return 'YES'

t = int(input())
for t_itr in range(t):
    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = gridChallenge(grid)

    print(result)
