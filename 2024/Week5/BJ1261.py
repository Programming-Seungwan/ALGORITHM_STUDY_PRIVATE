from sys import stdin as s
s = open('./input.txt', 'rt')
M, N = list(map(int, s.readline().strip().split()))
maze = [list(map(int, s.readline().strip())) for _ in range(N)]
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

# print(maze)
distance = [[float('inf')] * M for _ in range(N)]
# print(distance)

for j in range(N):
  for i in range(M):
    if i == 0 and j == 0:
      distance[j][i] = 0
      continue
    if maze[j][i] == 1: # 벽을 부숴야 들어갈 수 있는 경우에
      for k in range(4):
        ey = j + dy[k]
        ex = i + dx[k]
        if 0 <= ey < N and 0 <= ex < M:
          if distance[ey][ex] + 1 < distance[j][i]:
            distance[j][i] = distance[ey][ex] + 1
    if maze[j][i] == 0:
      for k in range(4):
        ey = j + dy[k]
        ex = i + dx[k]
        if 0 <= ey < N and 0 <= ex < M:
          if distance[ey][ex] < distance[j][i]:
            distance[j][i] = distance[ey][ex]

print(distance[N - 1][M - 1])