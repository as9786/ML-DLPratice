import sys 
# 재귀 제한 설정
sys.setrecursionimit(10000)

# 깊이 우선 탐색
def DFS(x: int, y: int):
    # Direction list
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    # 탐색 시작
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if (0 <= nx <m) and (0 <= ny < n):
            if cabbage[ny][nx] == 1:
                cabbage[ny][nx] = 0
                dfs(nx, ny)
                
# Numer of test case
T = int(sys.stdin.readline())

for _ in range(T):
    # 입력
    m, n, k = map(int, sys.stdin.realine().split())
    # 밭 생성
    cabbage = [[0 for _ in range(m)] for _ in range(n)]
    # 지렁이 개수 초기화
    c = 0
    
    # 배추 영역 
    for _ in range(k):
        x, y = map(int, sys.stdin.realine().split())
        cabbage[y][x] = 1
    
    for x in range(m):
        for y in range(n):
            if cabbage[y][x] == 1:
                dfs(x, y)
                c += 1 
                
    print(c)