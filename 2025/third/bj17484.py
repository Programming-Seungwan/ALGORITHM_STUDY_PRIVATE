from sys import stdin as s

s = open('./input.txt', 'rt')
[N, M] = list(map(int, s.readline().strip().split()))

fuelList = [list(map(int, s.readline().strip().split())) for _ in range(N)]
memo = [[0] * M for _ in range(N + 1)]

# 첫줄은 잘 채워넣기
for i in range(M):
  memo[1][i] = fuelList[0][i]

# # 두번째줄 채워넣기
# memo[2][0] = fuelList[1][0] + min(fuelList[0][0], fuelList[0][1])
# memo[2][M - 1] = fuelList[1][M - 1] + min(fuelList[0][M - 2], fuelList[0][M - 1])

# # 두 번째 줄 가운데 애들
# for i in range(1, M - 1):
#   memo[1][i] = fuelList[1][i] + min(fuelList[0][i - 1], fuelList[0][i], fuelList[0][i + 1])

for i in range(2, N + 1):
  for j in range(M):
    memoLine = memo[i - 2]
    fuelLine = fuelList[i - 2]
    if j == 0:
      memo[i][j] = fuelList[i - 1][j] + min(memo[i - 2][j + 2] + fuelList[i - 2][j + 1], memo[i - 2][j + 1] + fuelList[i - 2][j + 1], memo[i - 2][j] + fuelList[i - 2][j + 1], memo[i - 2][j + 1] + fuelList[i - 2][j])
    elif j == 1:
      memo[i][j] = fuelList[i - 1][j] + min(memo[i - 2][j - 1] + fuelList[i - 2][j - 1], memo[i - 2][j - 1] + fuelList[i - 2][j], memo[i - 2][j] + fuelList[i - 2][j - 1], memo[i - 2][j] + fuelList[i - 2][j + 1], memo[i - 2][j + 1] + fuelList[i - 2][j + 1], memo[i - 2][j + 1] + fuelList[i - 2][j], memo[i - 2][j + 2], fuelList[i - 2][j + 1])
    elif(j == M - 1):
      memo[i][j] = fuelList[i - 1][j] + min(memo[i - 2][j - 2] + fuelList[i - 2][j - 1], memo[i - 2][j - 1] + fuelList[i - 2][j - 1], memo[i - 2][j] + fuelList[i - 2][j - 1], memo[i - 2][j - 1] + fuelList[i - 2][j])
    elif (j == M - 2):
      memo[i][j] = fuelList[i - 1][j] + min(memoLine[j - 2] + fuelLine[j - 1],  memoLine[j - 1] + fuelLine[j - 1], memoLine[j] + fuelLine[j - 1], memoLine[j - 1] + fuelLine[j], memoLine[j + 1]+ fuelLine[j], memoLine[j] + fuelLine[j + 1], memoLine[j+ 1] + fuelLine[j + 1])
    else:
      memo[i][j] = fuelList[i - 1][j] + min(memoLine[j - 2] + fuelLine[j - 1],  memoLine[j - 1] + fuelLine[j - 1], memoLine[j] + fuelLine[j - 1], memoLine[j - 1] + fuelLine[j], memoLine[j + 1]+ fuelLine[j], memoLine[j] + fuelLine[j + 1], memoLine[j+ 1] + fuelLine[j + 1], memoLine[j + 2] + fuelLine[j + 1])

print(memo)