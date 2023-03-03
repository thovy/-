from collections import deque
import sys;
n, m = map(int, sys.stdin.readline().split())

visited = [0] * (n+1)
answer = []

def dfs(num):
    if num == m:
        print(' '.join(map(str, answer)))
        return
    
    for i in range(1,n+1):
        if visited[i] == 0:
            visited[i] += 1
            answer.append(i)
            dfs(num+1)
            visited[i] -= 1
            answer.pop()

dfs(0)