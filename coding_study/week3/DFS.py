def DFS(graph, v, visited):
    # 현재 node를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 node와 연결된 다른 node를 재귀적 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            
