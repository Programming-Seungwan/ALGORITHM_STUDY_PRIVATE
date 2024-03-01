# 적록 색약의 입장에서 R과 G는 같은 것임
from sys import stdin as s
from copy import deepcopy
from collections import deque
s = open('./input.txt', 'rt')
n = int(s.readline().strip())
myMap = [list(s.readline().strip()) for _ in range(n)]
secondMyMap = deepcopy(myMap)
visitedOne = [[False] * n for _ in range(n)]
visitedTwo = [[False] * n for _ in range(n)]

# 특정 문자열을 받아서 지도에 해당하는 섬을 잡는 것 한번 실행될 때마다 카운트는 올라감
dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]
def normalBfs(character, nY, nX):
  queue = deque()
  queue.append([nY, nX])

  while queue:
    tmpY, tmpX = queue.popleft()

    for i in range(4):
      nextY = tmpY + dy[i]
      nextX = tmpX + dx[i]
      if 0 <= nextY < n and 0 <= nextX < n:
        if visitedOne[nextY][nextX] == False and myMap[nextY][nextX] == character:
          visitedOne[nextY][nextX] = True
          queue.append([nextY, nextX])

# 해당 함수는 내부에서 r인지 g인지 체크를 함
def rgBfs(character, nY, nX):
  flag = True if (character == 'R' or character == 'G') else False # 해당 색깔이 r이나 g이면 True로, 아니면 False로 진행함
  queue = deque()
  queue.append([nY, nX])

  while queue:
    tmpY, tmpX = queue.popleft()
    for i in range(4):
      nextY = tmpY + dy[i]
      nextX = tmpX + dx[i]
      if 0<= nextY < n and 0 <= nextX < n:
        if flag == True:
          if visitedTwo[nextY][nextX] == False and (secondMyMap[nextY][nextX] == 'R' or secondMyMap[nextY][nextX] == 'G'):
            visitedTwo[nextY][nextX] = True
            queue.append([nextY, nextX])
        else:
          if visitedTwo[nextY][nextX] == False and secondMyMap[nextY][nextX] == character:
            visitedTwo[nextY][nextX] = True
            queue.append([nextY, nextX])

resultOne = 0
for j in range(n):
  for i in range(n):
    if visitedOne[j][i] == False:
      normalBfs(myMap[j][i], j, i)
      resultOne += 1

resultTwo = 0
for j in range(n):
  for i in range(n):
    if visitedTwo[j][i] == False:
      rgBfs(myMap[j][i], j, i)
      resultTwo += 1

print(resultOne, resultTwo)
