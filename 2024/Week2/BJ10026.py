from sys import stdin as s
from collections import deque
import copy

#s = open('./input.txt', 'rt')

N = int(s.readline().strip())

totalMap = []
for _ in range(N):
  tmpList = list(s.readline().strip())
  totalMap.append(tmpList)

rgTotalMap = copy.deepcopy(totalMap)


# 그냥 따로 맵을 만들어서 모든 초록색은 적색으로 만들어준다
for j in range(N):
  for i in range(N):
    if rgTotalMap[j][i] == 'G':
      rgTotalMap[j][i] = 'R'

checkMapOne = [[False] * N for _ in range(N)]
checkMapTwo = [[False] * N for _ in range(N)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

# 그냥 bfs는 일반인 시각에서의 bfs이다. 즉, checkMapOne에 기록을 하며 나아간다
def bfs(y, x):
  startColor = totalMap[y][x]
  queue = deque()
  checkMapOne[y][x] = True
  queue.append((y, x))

  while queue:
    ey, ex = queue.pop()
    for i in range(4):
      ny = ey + dy[i]
      nx = ex + dx[i]

      if 0 <= ny < N and 0 <= nx < N:
        if totalMap[ny][nx] == startColor and checkMapOne[ny][nx] == False:
          checkMapOne[ny][nx] = True
          queue.append((ny, nx))

# 이건 적록색약인 입장에서의 bfs이다.
def rgBfs(y, x):
  startColor = rgTotalMap[y][x]
  queue = deque()
  checkMapTwo[y][x] = True
  queue.append((y, x))

  while queue:
    ey, ex = queue.pop()
    for i in range(4):
      ny = ey + dy[i]
      nx = ex + dx[i]

      if 0 <= ny < N and 0 <=nx < N:
        if rgTotalMap[ny][nx] == startColor and checkMapTwo[ny][nx] == False:
          checkMapTwo[ny][nx] = True
          queue.append((ny, nx))

normalCount = 0
for j in range(N):
  for k in range(N):
    if checkMapOne[j][k] == False:
      bfs(j, k)
      normalCount += 1


rgPeopleCount = 0
for j in range(N):
  for i in range(N):
    if checkMapTwo[j][i] == False:
      rgBfs(j, i)
      rgPeopleCount += 1

print(normalCount, rgPeopleCount)