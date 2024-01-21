from sys import stdin as s
from collections import deque
from copy import deepcopy

s = open('./input.txt', 'rt')

M, N, H = list(map(int, s.readline().strip().split(' ')))
tomatoStorage = []
for _ in range(H):
  tmpList = []
  for i in range(N):
    tmpList.append(list(map(int, s.readline().strip().split(' '))))
  tomatoStorage.append(tmpList)

originalCheckMap = [[[False for _ in range(H)] for _ in range(N)] for _ in range(M)]


totalTomatoCount = 0

for i in range(H):
  for j in range(N):
    for k in range(M):
      if tomatoStorage[i][j][k] == 1 or tomatoStorage[i][j][k] == 0:
        totalTomatoCount += 1

def countWellDoneTomato():
  result = 0
  for i in range(H):
    for j in range(N):
      for k in range(M):
        if tomatoStorage[i][j][k] == 1:
          result += 1
  return result

# 인접한 토마토의 방향은 총 6가지이다.
dZ = [0, 0, 0, 0, 1, -1]
dY = [1, -1, 0, 0, 0, 0]
dX = [0, 0, 1, -1, 0, 0]

# 현재의 토마토들을 기반으로 더 익혀가는 함수를 의미한다
def bfs(z, y, x):
  checkMap = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]
  checkMap[z][y][x] = True
  queue = deque()
  queue.append((z, y, x))

  while queue:
    ez, ey, ex = queue.pop()
    for i in range(6):
      nz = ez + dZ[i]
      ny = ey + dY[i]
      nx = ex + dX[i]
      if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:
        if checkMap[ez][ey][ex] == False and tomatoStorage[ez][ey][ex] == 1 and tomatoStorage[nz][ny][nx] == 0:
          checkMap[ez][ey][ex] = True
          tomatoStorage[nz][ny][nx] = 1
          queue.append((nz, ny, nx))


dayCount = 0
def nearbyZero(i, j, k):
  for s in range(6):
    tmpz = i + dZ[s]
    tmpy = j + dY[s]
    tmpx = k + dX[s]

    if  0 <= tmpz < H and 0 <= tmpy < N and 0 <= tmpx < M:
      if tomatoStorage[tmpz][tmpy][tmpx] == 0:
        return True
  return False

for i in range(H):
  for j in range(N):
    for k in range(M):
      if tomatoStorage[i][j][k] == 1 and nearbyZero(i, j, k):
        bfs(i, j, k)
        dayCount += 1

wellDoneTomatoCount = countWellDoneTomato()

if wellDoneTomatoCount == totalTomatoCount:
  print(dayCount)
else:
  print(-1)