N, M = map(int, input().split())

basket = [0] * (N+1)
for n in range(1, N+1):
    basket[n] = n

for _ in range(M):
    i, j = map(int, input().split());
    while i < j:
        if j - i < 2:
            tmp = basket[i]
            basket[i] = basket[j]
            basket[j] = tmp
            break
        tmp = basket[i]
        basket[i] = basket[j]
        basket[j] = tmp
        i = i + 1
        j = j - 1
    
print(' '.join(map(str, basket[1:])));