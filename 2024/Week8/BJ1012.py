from sys import stdin as s
from collections import deque
#s = open('./input.txt', 'rt')
count = int(s.readline())
result = 0
resultList = []
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
def solution(bc, mm, positionY, positionX, endY, endX):
  global result
  queue = deque()
  queue.append([positionY, positionX])

  while queue:
    tmpY, tmpX = queue.pop()
    for i in range(4):
      eY = tmpY + dy[i]
      eX = tmpX + dx[i]
      if 0 <= eY < endY and 0 <= eX < endX:
        if bc[eY][eX] == 1 and mm[eY][eX] == False:
          mm[eY][eX] = True
          queue.append([eY, eX])

  result += 1

for _ in range(count):
  m, n, k = list(map(int, s.readline().strip().split()))
  baechoo = [[0] * m for _ in range(n)]
  memo = [[False ] * m for _ in range(n)]
  for _ in range(k):
    x, y = list(map(int, s.readline().strip().split()))
    baechoo[y][x] = 1
  for i in range(n):
    for j in range(m):
      if baechoo[i][j] == 1 and memo[i][j] == False:
        solution(baechoo, memo, i, j, n, m)
  resultList.append(result)
  result = 0

# print(resultList)
for i in range(count):
  print(resultList[i])