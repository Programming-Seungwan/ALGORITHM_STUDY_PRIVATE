import sys
input = sys.stdin.readline
import heapq
dx = [-1, 0 ,1 ,0]
dy = [0, 1, 0, -1]
inf = int(1e9) # 큰 수를 나타내기 위한 장치에 해당한다

def dijkstra(t, graph, dist):
    que = []
    dist[0][0] = graph[0][0]

    heapq.heappush(que, (dist[0][0], 0, 0)) # 특정 노드까지 가기위한 거리, x좌표, y 좌표를 저장한다. 그래야 heapq 자료구조에서 사용 가능

    while que:
        cost, x, y = heapq.heappop(que)

        if dist[x][y] < cost:
            continue

        for i in range(4): # 상하 좌우로 이동하면서 유효한 좌표인지를 먼저 검사하고 괜찮으면 존의 가치보다 낮으면 갈아끼운다
            nx = dx[i] + x
            ny = dy[i] + y
            if n > nx >= 0 and n > ny >= 0 :
                temp = cost + graph[nx][ny]
                if temp < dist[nx][ny]:
                    dist[nx][ny] = temp
                    heapq.heappush(que, (temp, nx, ny))

    print('Problem {}: {}'.format(t, dist[n - 1][n - 1]))


t = 1

while 1:
    n = int(input())
    graph = []
    if not n:
        break

    for i in range(n):
        graph.append(list(map(int, input().split())))

    dist = [[inf for i in range(n)] for j in range(n)]
    dijkstra(t, graph, dist)

    t += 1
