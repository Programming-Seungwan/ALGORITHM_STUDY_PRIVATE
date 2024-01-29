# 빙산이 분리되는 최초의 시간(년 단위)을 구하는 문제
# 빙산을 한칸 단위가 아닌, 1년 단위로 한번에 갱신해야됨, 1년이 지날 때마다 빙산이 총 몇 덩이인지 bfs로 구해줘야함
from sys import stdin as s
from collections import deque
s = open('./input.txt', 'rt')

N, M = list(map(int, s.readline().strip().split()))
year = 0
islandNumber = 0

seaMap = [list(map(int, s.readline().strip().split())) for _ in range(N)]
updateMapList = [[0] * M for _ in range(N)]

dY = [1, 0, -1, 0]
dX = [0, 1, 0, -1]

def countAdjacentZero(yIndex, xIndex):
  result = 0

  if seaMap[yIndex][xIndex] > 0:
    for i in range(4):
      tmpYIndex = yIndex + dY[i]
      tmpXIndex = xIndex + dX[i]
      if 0 <= tmpYIndex < N and 0 <= tmpXIndex < M:
        if seaMap[tmpYIndex][tmpXIndex] == 0:
          result += 1

  return result

# 현재의 지도를 바탕으로 섬이 몇개인지를 세주는 함수
def countIslandNumber(mapOfSea):
  count = 0
  check = [[False] * M for _ in range(N)]
  def countRecur(y, x):
    queue = deque()
    queue.append((y, x))
    check[y][x] = True

    while queue:
      tmpY, tmpX = queue.pop()
      for j in range(4):
        nextY = tmpY + dY[j]
        nextX = tmpX + dX[j]
        if 0 <= nextY < N and 0 <= nextX < M:
          if check[nextY][nextX] == False:
            queue.append((nextY, nextX))
            check[nextY][nextX] = True
  for k in range(N):
    for u in range(M):
      if mapOfSea[k][u] != 0 and check[k][u] == False:
        countRecur(k, u)
        count += 1
  return count

while True:
  for t in range(N):
    for s in range(M):
      updateMapList[t][s] = countAdjacentZero(t, s)
  for j in range(N):
    for i in range(M):
      seaMap[j][i] = seaMap[j][i] - updateMapList[j][i] # 다음에 updateMapList를 갱신할 필요가 있는가?
  updateMapList = [[0] * M for _ in range(N)]
  year += 1
  islandNumber = countIslandNumber(seaMap)
  if islandNumber >= 2:
    break
  if islandNumber == 0:
    break

if islandNumber > 2:
  print(year)
else:
  print(0)
