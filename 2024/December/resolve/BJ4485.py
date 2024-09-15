# Dijkstra 알고리즘과 연관된 문제
# from sys import stdin as s
import heapq
s = open('./input.txt', 'rt')
dx = [-1, 0 ,1, 0]
dy = [0, 1, 0, -1]
inf = int(1e9)

def getMinCostDijkstra(n, graph, dist):
  queue = [] # 모든 노드를 넣어놓을 배열에 해당함
  dist[0][0] = graph[0][0] # 시작 노드는 무조건 기록이 되어야 하므로 넣어줌

  heapq.heappush(queue, (dist[0][0], 0, 0)) # 시작 노드를 넣는다.

  while queue: # 큐에 넣어놓고 빌떄까지 로직을 돌리는 것은 굉장히 흔한 알고리즘임!
    cost, x, y = heapq.heappop(queue)

    if dist[x][y] < cost:
      continue

    for i in range(4):
      nx = dx[i] + x
      ny = dy[i] + y

      if n > nx >= 0 and n > ny >= 0:
        tmp = cost + graph[nx][ny]
        if (tmp < dist[nx][ny]):
          dist[nx][ny] = tmp
          heapq.heappush(queue, (tmp, nx, ny))
  print('Problem {}: {}'.format(n, dist[n - 1][n - 1]))

num = 1

while True:
  k = int(s.readline())
  graph = []

  if not k:
    break

  for _ in range(k):
    graph.append(list(map(int, s.readline().split())))

  dist = [[inf for i in range(k)] for j in range(k)]
  getMinCostDijkstra(num, graph, dist)
  num += 1

