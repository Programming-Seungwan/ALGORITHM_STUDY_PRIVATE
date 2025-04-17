from sys import stdin as s

s = open('./input.txt', 'rt')
[N, M] = list(map(int, s.readline().strip().split()))

fuelList = [list(map(int, s.readline().strip().split())) for _ in range(N)]
memo = [[0] * M for _ in range(N)]

# 첫줄은 잘 채워넣기
for i in range(M):
  memo[0][i] = fuelList[0][i]

# 두번째줄 채워넣기
memo[1][0] = fuelList[1][0] + min(fuelList[0][0], fuelList[0][1])
memo[1][M - 1] = fuelList[1][M - 1] + min(fuelList[0][M - 2], fuelList[0][M - 1])

# 두 번째 줄 가운데 애들
for i in range(1, M - 1):
  memo[1][i] = fuelList[1][i] + min(fuelList[0][i - 1], fuelList[0][i], fuelList[0][i + 1])

for i in range(2, N):
  for j in range(M):
    if j == 0:
      memo[i][0] = min(memo[i - 2][0] + fuelList[i - 1][1] + fuelList[i][0], memo[i - 2][1] + fuelList[i - 1][0] + fuelList[i][0])
    elif(j == M - 1):
      memo[i][j] = min(memo[i - 2][j] + fuelList[i - 1][j - 1] + fuelList[i][j], memo[i - 2][j - 1] + fuelList[i - 1][j - 1] + fuelList[i][j])
    else:
      memo[i][j] = min(memo[i - 2][j - 1] + fuelList[i - 1][j - 1] + fuelList[i][j], memo[i - 2][j + 1] + fuelList[i - 1][j + 1] + fuelList[i][j])

print(memo)