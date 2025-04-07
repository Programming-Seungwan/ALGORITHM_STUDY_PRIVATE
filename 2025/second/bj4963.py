import sys
sys.setrecursionlimit(10 ** 4)
from sys import stdin as s

s = open('./input.txt', 'rt')

sampleTwoDimensionList =[[1, 0, 1, 0, 0], [1, 0, 0, 0, 0], [1, 0, 1, 0, 1], [1, 0, 0, 1, 0]]

dx = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 0, 1, 1, 1]

# dfs 알고리즘으로 풀어야 함
# 섬의 개수를 셀 count 변수, 원본 대상 array, 마킹할 array
# 왔다 갔냐를 의미하므로, 기본값은 false이되, 바다는 true로 설정하기
# false를 만나면 dfs를 시작하기.
# dfs는 자기 주변을 돌면서 점령해나가기

def dfs(mapTwoDimensionList, markingList, y, x):
  xLength = len(mapTwoDimensionList[0])
  yLength = len(mapTwoDimensionList)
  for i in range(0, 9):
    nextX = x + dx[i]
    nextY = y + dy[i]
    if (0 <= nextX < xLength and 0 <= nextY < yLength and markingList[nextY][nextX] == False):
      markingList[nextY][nextX] = True # 왔다 간 것으로 정리하기
      dfs(mapTwoDimensionList, markingList, nextY, nextX)

def solution(realList):
  xLength = len(realList[0])
  yLength = len(realList)

  solutionMarkingList = [[cell == 0 for cell in row] for row in realList]
  count = 0
  for i in range(yLength):
    for j in range(xLength):
      if (solutionMarkingList[i][j] == False):
        dfs(realList, solutionMarkingList, i, j)
        count += 1
  return count

while True:
  newString = s.readline().strip()
  if (newString == '0 0'):
    break
  [xlen, ylen] = list(map(int, newString.split()))
  tmpMapList = []
  for y in range(ylen):
      tmpMapList.append(list(map(int, s.readline().strip().split())))

  print(solution(tmpMapList))