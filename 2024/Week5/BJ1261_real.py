import heapq

M, N = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
distance = [[1e10] * M for _ in range(N)]

dr = [-1, 0, 1, 0]  # 상 우 하 좌
dc = [0, 1, 0, -1]  # 상 우 하 좌


def dijkstra():
    q = []
    heapq.heappush(q, (0, 0, 0)) # 튜플의 첫번째 요소를 기준으로 최소 히프는 내부 정렬된다
    distance[0][0] = 0
    while q:
        cost, r, c = heapq.heappop(q)

        if cost > distance[r][c]:
            continue

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= M:  # 범위를 벗어나거나 이미 방문했으면 진행x
                continue

            if cost + arr[nr][nc] < distance[nr][nc]:
                distance[nr][nc] = cost + arr[nr][nc]
                heapq.heappush(q, (distance[nr][nc], nr, nc))


dijkstra()
print(distance[N - 1][M - 1])