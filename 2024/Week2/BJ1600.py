from sys import stdin as stdin
from collections import deque

s = open('./input.txt', 'rt')

K = int(s.readline().strip())

# W는 가로이고 H는 높이
W, H = list(map(int, s.readline().strip().split(' ')))

totalMap = [list(map(int, s.readline().strip().split(' '))) for _ in range(H)]
checkMap = [[0] * W for _ in range(H)]

# 말로서의 움직임 + 일반 움직임
horseDY = [1, 2, 2, 1, -2, -1, -1, -2, 1, 0, -1, 0]
horseDX = [2, 1, -1, -2, -1, -2, 2, 1, 0, 1, 0, -1]

# only 일반 움직임
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

# 말의 움직임인지를 체크하는 함수
def isHorseMove(moveY, moveX):
  if moveY == 1 and moveX == 2:
    return True
  if moveY == 2 and moveX == 1:
    return True
  if moveY == 2 and moveX == -1:
    return True
  if moveY == 1 and moveX == -2:
    return True
  if moveY == -2 and moveX == -1:
    return True
  if moveY == -1 and moveX == -2:
    return True
  if moveY == -1 and moveX == 2:
    return True
  if moveY == -2 and moveX == 1:
    return True

  return False


def bfs(y, x):
  horseMoveCount = 0
  queue = deque()
  queue.append((y,x))
  checkMap[y][x] = 0

  while queue:
    ey, ex = queue.pop()
    # 원숭이 움직임을 체크해서 다 채웠으면 일반움직임을, 아니면 포함을 돌려야 한다
    if ey == H - 1 and ex == W - 1:
      return checkMap[H - 1][W - 1]

    if horseMoveCount < K:
      for i in range(12):
        ny = ey + horseDY[i]
        nx = ex + horseDX[i]
        if 0 <= ny < H and 0 <= nx < W:
          if totalMap[ny][nx] == 0 and checkMap[ny][nx] == 0:
            if isHorseMove(horseDY[i], horseDX[i]):
              horseMoveCount += 1
            checkMap[ny][nx] = checkMap[ey][ex] + 1
            queue.append((ny, nx))
            if (horseMoveCount >= K): break
    else:
      for i in range(4):
        ny = ey + dy[i]
        nx = ex + dx[i]
        if 0 <= ny < H and 0 <= nx < W:
          if totalMap[ny][nx] == 0 and checkMap[ny][nx] == 0:
            checkMap[ny][nx] = checkMap[ey][ex] + 1
            queue.append((ny, nx))


  return -1

print(bfs(0,0))