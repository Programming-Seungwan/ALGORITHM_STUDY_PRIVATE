# 빙산이 분리되는 최초의 시간(년 단위)을 구하는 문제
# 빙산을 한칸 단위가 아닌, 1년 단위로 한번에 갱신해야됨, 1년이 지날 때마다 빙산이 총 몇 덩이인지 bfs로 구해줘야함
import sys
sys.setrecursionlimit(10 ** 6)

N, M = list(map(int, input().split()))
year = 0
islandNumber = 0

seaMap = [list(map(int, input().split())) for _ in range(N)]
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
def countIslandNumber(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    def dfs(i, j):
        if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0 or visited[i][j]:
            return
        visited[i][j] = True  # Mark as visited
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != 0 and not visited[i][j]:
                dfs(i, j)
                count += 1

    return count


while True:
  for t in range(N):
    for s in range(M):
      updateMapList[t][s] = countAdjacentZero(t, s)
  for j in range(N):
    for i in range(M):
      seaMap[j][i] = seaMap[j][i] - updateMapList[j][i] if (seaMap[j][i] - updateMapList[j][i]) > 0 else 0  # 다음에 updateMapList를 갱신할 필요가 있는가?
  updateMapList = [[0] * M for _ in range(N)]
  # print(seaMap)
  year += 1
  islandNumber = countIslandNumber(seaMap)
  # print(islandNumber)
  # print(year)
  if islandNumber != 1:
     break

if islandNumber >= 2:
   print(year)
if islandNumber == 0:
   print(0)
