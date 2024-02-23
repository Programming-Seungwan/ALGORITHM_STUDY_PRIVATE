from sys import stdin as s
s = open('./input.txt', 'rt')
t, w = list(map(int, s.readline().strip().split()))
fruitList = [0]
for _ in range(t):
  fruitList.append(int(s.readline()))
memo = [[0] * (t + 1) for _ in range(w + 1)]

for i in range(1, t + 1):
  if fruitList[i] == 1:
    memo[0][i] = memo[0][i - 1] + 1
  else:
    memo[0][i] = memo[0][i - 1]

def myFun(moveCount):
  result = 1
  if (moveCount % 2 == 0):
    result = 1
  else:
    result = 2
  return result

for i in range(1, w + 1):
  for j in range(i, t + 1):
    # 이번 턴에서는 스위칭을 하지 않는 경우
    if myFun(i) == fruitList[j]:
      memo[i][j] = max(memo[i][j] + memo[i][j - 1] + 1, memo[i][j] + memo[i - 1][j] + 1)
    else:
      memo[i][j] = max(memo[i][j] + memo[i][j - 1], memo[i][j] + memo[i - 1][j])

print(memo[w][t])

