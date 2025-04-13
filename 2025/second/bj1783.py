from sys import stdin as s
s = open('./input.txt', 'rt')

# N은 세로, M은 가로임
[N, M] = list(map(int, s.readline().strip().split()))
memo = [[False] * (M + 1) for _ in range(N + 1)]
memo[N][1] = True

# print(memo)

dy = [-2, -1, 1, 2]
dx = [1, 2, 2, 1]

def dfs(memo, x, y):
  for i in range(4):
    nextX = x + dx[i]
    nextY = y + dy[i]
    if (1 <= nextY <= N and 1 <= nextX <= M):
      memo[nextY][nextX] = True
      dfs(memo, nextX, nextY)

dfs(memo, 1, N)

trueCount = 0

for i in range(1, N + 1):
  for j in range(1, M + 1):
    if (memo[i][j] == True):
      trueCount +=1
print(trueCount)
