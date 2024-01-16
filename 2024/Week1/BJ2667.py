from sys import stdin as s
from collections import deque

s = open('./input.txt', 'rt')

N = int(s.readline().strip())

checkMap = [[False] * N for _ in range(N)]
totalMap = []

for _ in range(N):
  tmpLineList = list(map(int, list(s.readline().strip())))
  totalMap.append(tmpLineList)


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

# 시작점부터 큐에 넣기 시작하여 넓이를 반환하는 함수
#bfs는 근처의 같은 레벨을 먼저 탐색하여 큐에 넣고 그 다음에 큐에서 뽑아서 가고 한다
def bfs(y, x):
  queue = deque()
  queue.append((y, x))

  resultArea = 1

  while queue:
    ey, ex = queue.pop()
    for u in range(4):
      ny = ey + dy[u]
      nx = ex + dx[u]

      if 0 <= ny < N and 0 <= nx < N:
        if totalMap[ny][nx] == 1 and checkMap[ny][nx] == False:
          checkMap[ny][nx] = True
          queue.append((ny, nx))
          resultArea += 1
  return resultArea


result = [] # 이는 단지 너비 결과들을 담을 배열에 해당한다

for j in range(N):
  for i in range(N):
    # 2차원 배열을 순회하면서 큐가 빌때까지 bfs를 돌리면서 카운트를 늘려가야함
    if totalMap[j][i] == 1 and checkMap[j][i] == False:
      checkMap[j][i] = True
      tmpResult = bfs(j, i)
      result.append(tmpResult)

result.sort()

print(len(result))

for i in range(len(result)):
  print(result[i])

