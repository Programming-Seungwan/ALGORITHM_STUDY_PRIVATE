from sys import stdin as s
from collections import deque

s = open('./input.txt', 'rt')

startPoint, goalPoint = list(map(int, s.readline().strip().split(' ')))

# 가능한 이동 지점을 돌려주는 함수
def move(caseNum, incomePoint):
  if caseNum == 0:
    return incomePoint + 1
  if caseNum == 1:
    return incomePoint - 1
  if caseNum == 2:
    return incomePoint * 2

memoArray = [0 for _ in range(100001)]
checkArray = [False for _ in range(100001)]

# bfs 함수는 목표에 맞는 지점을 발견하면 기록하고 break 한다

moveSecond = 0

def bfs(sPoint):
  queue = deque()
  queue.append(sPoint)
  global moveSecond

  while queue:
    eP = queue.pop()
    flag = False
    for i in range(3):
      nP = move(i, eP)

      if 0 <= nP <=100000:
        if checkArray[nP] == False:
          checkArray[nP] = True
          queue.append(nP)
          if flag == False:
            moveSecond += 1
            flag = True
          memoArray[nP] = moveSecond
          if (nP == goalPoint): return

bfs(startPoint)

print(memoArray[goalPoint])