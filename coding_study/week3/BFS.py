from collections import deque

def BFS(graph, start, visited):
    queue = deque([start])
    # 현재 node를 방문 처리
    visited[start] = True 
    # Queue가 빌 때까지 반복
    while queue:
        # Queue에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된 아직 방문하지 않은 원소들을 queue에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True 
                
                