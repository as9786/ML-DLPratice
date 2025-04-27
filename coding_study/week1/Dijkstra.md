# 최단 경로(Shorted path)

- 가장 짧은 경로를 찾는 algorithm
- 길 찾기 문제
- Graph representation. 각 지점 : node, 지점 간 연결된 도로 : 간선
- Ex) 다익스트라, 플로이드 워셜, 벨만 포드
- Greedy, DP의 종류

# Dijkstra shorted path algorithm
- 여러 개의 node가 있을 때, 특정한 node에서 출발하여 다른 node로 가는 각각의 최단 경로를 구하는 algorithm
- 음의 간선이 없을 때, 정상적으로 작동
- 음의 간선 : 0보다 작은 값을 가지는 간선
- 실제로 GPS software의 base algorithm
- Greedy algorithm
- 가장 비용이 적은 node를 선택해서 임의의 과정을 반복

1. Set start node
2. Init shorted path table
3. 방문하지 않은 node 중에서 최단 거리가 가장 짧은 node를 선택
4. 해당 node를 거쳐 다른 node로 가는 비용을 계산하여 shorted path table 갱신
5. 3번과 4번 방법

- 최단 거리 정보를 1D list에 저장하며 계속해서 갱신
- 매번 현재 처리하고 있는 node를 기준으로 주변 간선을 확인
- 한 단계당 하나의 node에 대한 최단 거리를 확실히 찾는 것