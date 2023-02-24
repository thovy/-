from collections import deque
def solution(maps):
    # answer = 0
    
#     # bfs
    
#     # 움직일 수 있는 범위 4 가지[x,y]
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
    
#     n = len(maps[0])
#     m = len(maps)
    
#     def bfs(x, y):
#         queue = deque()
#         queue.append((x,y))
#         while queue:
#             x, y = queue.popleft()
#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]
#                 if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                     continue
#                 if maps[nx][ny] ==0:
#                     continue
#                 if maps[nx][ny] == 1 or maps[nx][ny] > maps[x][y] + 1:
#                     maps[nx][ny] = maps[x][y] + 1
#                     queue.append((nx,ny))
#         return maps[n-1][m-1] if maps[n-1][m-1] != 1 else -1
    
    def bfs(y, x):
        q = deque()
        q.append((y, x, 1))

        while q:
            y, x, distance = q.popleft()

            if y == len(maps)-1 and x == len(maps[0])-1:
                return distance

            if maps[y][x] == 0:
                continue
            maps[y][x] = 0

            if y+1 < len(maps):
                q.append((y+1, x, distance+1))
            if x+1 < len(maps[0]):
                q.append((y, x+1, distance+1))
            if y-1 >= 0:
                q.append((y-1, x, distance+1))
            if x-1 >= 0:
                q.append((y, x-1, distance+1))
        # while 에서 return 이 안 되었다면 갈 수 없는 거므로 -1 리턴
        return -1
    
    answer = bfs(0,0)
    
    return answer