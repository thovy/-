import sys
n, m = map(int, sys.stdin.readline().split())

answer = []

def dfs(idx):
    if len(answer) == m:
        print(*answer)
        return
    
    for i in range(idx, n):
        answer.append(i+1)
        dfs(i+1)
        answer.pop()
dfs(0)
    