N, M = map(int, input().split())

basket = [0] * (N+1)
for n in range(1, N+1):
    basket[n] = n

for _ in range(M):
    i, j = map(int, input().split());
    tmp = basket[i];
    basket[i] = basket[j];
    basket[j] = tmp
    
print(' '.join(map(str, basket[1:])));