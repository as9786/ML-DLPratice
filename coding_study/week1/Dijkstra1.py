# Library
import sys 
input = sys.stdin.readline 

# Number of node and edge
n, m = map(int, input().split())
# Start node
start = int(input())
# Graph
graph = [[] for i in range(n+1)]
# Visited list
visited = [False] * (n+1)
# Shorted path table
distance = [float('inf')] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a node to b node. Cost c
    graph[a].append((b,c))
    
# 방문하지 않은 node 중에서, 가장 최단 거리가 짧은 node의 번호를 반환
def get_smallest_node():
    min_value = float('inf')
    # 가장 최단 거리가 짧은 식별자
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i 
    return index 

def dijkstra(start):
    # Init start node
    distance[start] = 0
    visited[start] = True 
    for j in graph[start]:
        distance[j[0]] = j[1]
        
    # Start node를 제외한 전체 n-1개의 node에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 node를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True 
        # Current node와 연결된 다른 node 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 node를 거쳐서 다른 node로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost 

# 실행                
dijkstra(start)

# 최단 거리 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우
    if distance[i] == float('inf'):
        print('Infinity')
        
    else:
        print(distance[i])