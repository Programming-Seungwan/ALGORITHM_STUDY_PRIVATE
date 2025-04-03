import sys
sys.setrecursionlimit(10 ** 4)

from sys import stdin as s


s = open("./input.txt", "rt")

# 안전한 영역의 최대 개수를 구하는 법 -> dfs를 이용하여 체크를 함
# dfs를 구현하는 법
# 특정 배열을 계속 순회하며 체크테이블을 검사해 나간다.
# 인접 노드를 탐색할 떄, 상하좌우를 도는데, 이는 dx와 dy 배열을 통해서 하며 요소 검사도 한다.

n = int(s.readline().strip())

infoList = [list(map(int, s.readline().strip().split())) for _ in range(n)]
maxHeight = max(map(max, infoList)) # 예제에서는 9

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(x, y, visited): # 해당 인자들은 이미 주어진 데이터라고 가정, 즉 안 바뀜
  # 기존꺼 돌면서 검사하기. 이미 함수가 실행되었다는 것은, 해당 칸은 아직 방문 안 됐다는 것.
  for i in range(0, 4):
    nextX = x + dx[i]
    nextY = y + dy[i]
    # 특정 칸이 유효하다는 조건 하에, 아직 방문 안됐으면 true로 바꾸고 재귀함수

    if (nextX >= 0 and nextX < n and nextY >= 0 and nextY < n and visited[nextX][nextY] == False):
      visited[nextX][nextY] = True
      dfs(nextX, nextY, visited)

answer = 1

for tmpHeight in range(1, maxHeight + 1):
  visited = [[False] * n for _ in range(n)]
  for j in range(0, n):
    for k in range(0, n):
      if infoList[j][k] <= tmpHeight:
        visited[j][k] = True

  count = 0
  for x in range(0, n):
    for y in range(0, n):
      if (visited[x][y] == False):
        dfs(x, y, visited)
        count += 1

  answer = max(answer, count)

print(answer)

