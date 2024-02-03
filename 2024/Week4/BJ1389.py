from sys import stdin as s
from collections import deque
s = open('./input.txt', 'rt')
userNum, relationShipNum = list(map(int, s.readline().strip().split()))
relationDic = {}
visitedList = [[-1] * (userNum + 1) for _ in range(userNum + 1)] # 0 인덱스는 따로 사용하지 않는다

for i in range(1, userNum + 1):
  relationDic[i] = []
for i in range(relationShipNum):
  firstNode, secondNode = list(map(int, s.readline().strip().split()))
  if secondNode not in relationDic[firstNode]:
    relationDic[firstNode].append(secondNode)
  if firstNode not in relationDic[secondNode]:
    relationDic[secondNode].append(firstNode)


def recur(originUser):
  count = 1
  queue = deque()

  for i in range(len(relationDic[originUser])):
    queue.append(relationDic[originUser][i])
    visitedList[originUser][relationDic[originUser][i]] = count

  while queue:
    tmpNode = queue.pop()

    for i in range(len(relationDic[tmpNode])):
      if visitedList[originUser][relationDic[tmpNode][i]] == -1:
        visitedList[originUser][relationDic[tmpNode][i]] = visitedList[originUser][tmpNode] + 1
        queue.append(relationDic[tmpNode][i])

for i in range(userNum):
  recur(i + 1)
result = [0 for _ in range(userNum + 1)]

for i in range(1, userNum + 1):
  sum = 0
  for j in range(1, userNum + 1):
    if i != j:
      sum += visitedList[i][j]
  result[i] = sum

resultIndex = 1
resultSum = result[1]
for i in range(2, userNum + 1):
  if result[i] < resultSum:
    resultSum = result[i]
    resultIndex = i

print(resultIndex)