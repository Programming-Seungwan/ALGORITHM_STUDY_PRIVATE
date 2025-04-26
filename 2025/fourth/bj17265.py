from sys import stdin as s
s = open('./input.txt','rt')
N = int(s.readline().strip())

mapList = [s.readline().strip().split(' ') for _ in range(N)]
dy = [0, 1]
dx = [1, 0]

visited = [[False] * N for _ in range(N)]

def decideChar(ch):
  if ch != '+' and ch!= '-' and ch!='*':
    return int(ch)
  else:
    return ch

resultList = []

def evaluateCalculation(calList):
  result = int(calList[0])
  length = len(calList)
  for i in range(1, length - 1, 2):
    if calList[i] == '+':
      result += int(calList[i + 1])
    elif calList[i] == '-':
      result -= int(calList[i + 1])
    elif calList[i] == '*':
      result *= int(calList[i + 1])

  return result


def backtracking(x, y, calculation):
  if x == N - 1 and y == N - 1:
    resultList.append(evaluateCalculation(calculation))

  for i in range(2):
    nextX = x + dx[i]
    nextY = y + dy[i]
    # 들어갈 수 있는 애면 체크하고 처리하고
    if (0 <= nextX < N and 0 <= nextY < N ):
      if (visited[nextY][nextX] == False):
        visited[nextY][nextX] = True
        calculation.append(mapList[nextY][nextX])
        backtracking(nextX, nextY, calculation)
        calculation.pop()
        visited[nextY][nextX] = False



backtracking(0, 0, [mapList[0][0]])

print(max(resultList), min(resultList))