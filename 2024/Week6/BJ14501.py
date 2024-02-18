from sys import stdin as s
#s = open('./input.txt', 'rt')

N = int(s.readline().strip())
T = [0]
P = [0]
for i in range(N):
  time, pay = list(map(int, s.readline().strip().split()))
  T.append(time)
  P.append(pay)
resultList = [0 for _ in range(N + 1)]

def getMaxBeforeValue(ls, index):
  maxValue = 0
  for i in range(index):
    if maxValue < ls[i]:
      maxValue = ls[i]
  return maxValue

for i in range(1, N + 1):
  endTime = i + T[i] - 1
  if endTime > N:
    continue
  beforePrice = getMaxBeforeValue(resultList, i)
  if resultList[endTime] < beforePrice + P[i]:
    resultList[endTime] = beforePrice + P[i]

print(max(resultList))