from collections import deque
import sys 

input = sys.stdin.readline 

def bfs(x, y):
    queue = deque([(x,y)])
    a = 0
    while queue:
        x, y = queue.popleft()
        visited[x][y] = True 
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0 and visited[nx][ny] == False:
                a += 1
                queue.append((nx,ny))
    return a
    
# 입력
n, m = map(int,input().split())

# Init graph
graph = [[] for _ in range(n)]

# Visited graph
visited = [[False] * m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
# Create graph
for i in range(n):
    a = input().strip()
    for j in a:
        graph[i].append(int(j))

answer = 0

for i in range(n):
    for j in range(m):
        b = bfs(i, j)
        if b > 0:
            answer += 1

print(answer)


                
    
    
        
