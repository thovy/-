max_number = 0
max_x, max_y = 0, 0

for y in range(9):
    y_list = list(map(int, input().split()))
    this_max = max(y_list)
    if this_max > max_number:
        max_number = this_max
        max_y = y
        max_x = y_list.index(this_max)

print(max_number)
print(max_y+1, max_x+1)