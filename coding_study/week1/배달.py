# Library
import heapq

def solution(N, road, K):
    # 정답 값 초기화
    answer = 0
    
    # Set dijkstra algorithm
    graph = [[] for _ in range(N+1)]
    distance = [float('inf')] * (N+1)
    start = 1

    for i in range(len(road)):
        a, b, c = road[i]
        graph[a].append((b,c))
        graph[b].append((a,c))
    
    # Init heap
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))
                
    for j in range(1, N+1):
        if distance[j] <= K:
            answer += 1

    return answer