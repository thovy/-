
cube = []

max_len = 0

while True:
    try:
        # split 을 하지 않으니 원하는 대로 됨.
        tmp_list = list(map(str, input()))
        if max_len <= len(tmp_list):
            max_len = len(tmp_list)
        cube.append(tmp_list)
    except EOFError:
        break

for l in cube:
    if len(l) < max_len:
        gap = max_len - len(l)
        for _ in range(gap):
            l.append("")

col_cube = [ [""] * len(cube) for _ in range(max_len)]

for y in range(len(cube)):
    for x in range(max_len):
        col_cube[x][y] = cube[y][x]

answer = ''.join([''.join(row) for row in col_cube])
print(answer)
