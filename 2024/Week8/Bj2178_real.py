from collections import deque
N, M = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(input())

visited = [[-1] * M for _ in range(N)]
def bfs():
    visited[0][0] = 1
    q = deque()
    q.append((0, 0))

    dy = (-1, 1, 0, 0)
    dx = (0, 0, -1, 1)
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not (0 <= nx < M and 0 <= ny < N):
                continue

            if arr[ny][nx] == '1' and visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1
                q.append((ny, nx))

bfs()
print(visited[N-1][M-1])
