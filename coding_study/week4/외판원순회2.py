# Library
import sys 
input = sys.stdin.readline

# 입력
n = int(input())

# 도시 생성
graph = []
for _ in range(n):
    a = list(map(int,input().split()))
    graph.append(a)

# DFS
def dfs(start, ne, cost, visited):
    global min_cost 

    # 모든 도시를 방문 후, 마지막 도시에서 시작 도시로 돌아올 수 있는 경우, 재귀 종료
    if False not in visited: 
        if graph[ne][start] > 0:
            min_cost = min(min_cost, cost + graph[ne][start])
        return 

    for i in range(n):
        # 방문하지 않은 도시이며, 방문할 수 있는 경우에 현재 최소 비용보다 가는 비용이 적을 경우
        if graph[ne][i] > 0 and not visited[i] and cost < min_cost: 
            # 해당 도시 방문 처리
            visited[i] = True 
            # 재귀
            dfs(start, i, cost + graph[ne][i], visited)
            # 모든 방문이 끝나면 해당 도시 방문 취소
            visited[i] = False 

# 최소 비용 초기화
min_cost = 1e8

for i in range(n):
    visited = [False] * n
    visited[i] = True 
    dfs(i, i, 0, visited)

print(min_cost)
