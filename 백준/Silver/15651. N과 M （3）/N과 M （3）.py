import sys;
n, m = map(int, sys.stdin.readline().split())

answer = [0] * m

def dfs(num):
    if num == m:
        print(*answer)
        return
    
    for i in range(1, n+1):
        answer[num] = i
        dfs(num + 1)
dfs(0)