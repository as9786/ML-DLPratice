# Library
import heapq
import sys 
input = sys.stdin.readline 

# Number of node and edge
n, m = map(int, input().split())
# Start node
start = int(input())
# 각 node에 연결되어 있는 node에 대한 정보를 담는 list 
graph = [[] for i in range(n+1)]
# Shorted path table 
distance = [float('inf')] * (n+1)

# 모든 간선 정보
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    
def dijkstra(start):
    q = []
    # Start node로 가기 위한 최단 경로는 0으로 설정, queue에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    # Unless queue is empty
    while q:
        # 가장 최단 거리가 짧은 node에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 node가 이미 처리되었으면 무시
        if distance[now] < dist: 
            continue 
        # 현재 node와 연결된 다른 인접한 node들을 확인
        for i in graph[now]:
            cost = dist + i
            # 현재 node를 거쳐서, 다른 node로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost 
                heapq.heappush(q, (cost, i[0]))
                
dijkstra(start)

for i in range(1, n+1):
    if distance[i] == float('inf'):
        print('Infinity')
    else:
        print(distance[i])