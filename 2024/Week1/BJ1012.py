# 테스트 케이스의 개수를 구하고 그만큼 밭 2차원 리스트를 만든다.
# 해당 밭에서 몇 개의 조각이 있는지를 구한다.
from sys import stdin as s
from collections import deque

# s=open("./input.txt","rt")

number = int(s.readline().strip())

fieldsArray = [] # 이 리스트에 밭으로 표현될 2차원 리스트들이 저장됨
checksArray = [] # 각 밭마다 체크용으로 쓸 2차원 리스트들이 저장됨

for _ in range(number):
  m, n, baechooNum = list(map(int, s.readline().strip().split(' ') ))
  tmpFieldList = [[0] * n for j in range(m)]
  tmpCheckList = [[False] * n for k in range(m)]

  for i in range(baechooNum):
    tx, ty = list(map(int, s.readline().strip().split(' ')))
    tmpFieldList[tx][ty] = 1

  fieldsArray.append(tmpFieldList)
  checksArray.append(tmpCheckList)

dy = [0, 1, 0, -1]
dx = [1, 0 ,-1, 0]

def bfs(y, x, field, check):
  # check[0][0] = 1
  queue = []
  queue.append((y,x))

  verticalLength = len(field)
  horizontalLength = len(field[0])

  while queue:
    ey, ex = queue.pop()
    for u in range(4):
      ny = ey + dy[u]
      nx = ex + dx[u]

      if 0 <= ny < verticalLength and 0 <= nx < horizontalLength:
        if field[ny][nx] == 1 and check[ny][nx] == False:
          check[ny][nx] = True
          queue.append((ny, nx))




result = []


for q in range(number):
  count = 0
  tmpField = fieldsArray[q]
  checkField = checksArray[q]

  tmpFieldRow = len(tmpField)
  tmpFieldCol = len(tmpField[0])

  for j in range(tmpFieldRow):
    for i in range(tmpFieldCol):
      if tmpField[j][i] == 1 and checkField[j][i] == False:
        checkField[j][i] = True
        count += 1
        bfs(j, i, tmpField, checkField)
  result.append(count)

for i in range(len(result)):
  print(result[i])