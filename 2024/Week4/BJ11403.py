# 전형적인 dfs로 풀 수 있는 문제임 특정 점에서 시작하여 dfs를 진행하며 도착하는 모든 노드에 1을 기록한다.
from sys import stdin as s
#s = open('./input.txt', 'rt')
n = int(s.readline().strip())
informationList = [list(map(int, s.readline().strip().split())) for _ in range(n)]
visited = [] # 현재 턴에서 방문한 노드를 넣어놓을 리스트
result = [[0] * n for _ in range(n)]

def isLineEmpty(listNum):
  for i in range(n):
    if informationList[listNum][i] == 1:
      return False
  return True

# 본 함수의 발동 조건 : 1인 길이 있을 때 발동
def recur(originNodeIndex, newVisitedIndex):
  # print(newVisitedIndex)
  visited.append(newVisitedIndex)
  if originNodeIndex == newVisitedIndex:
    return

  for i in range(n):
    if informationList[newVisitedIndex][i] != 0 and not(i in visited) and not isLineEmpty(newVisitedIndex):
      recur(originNodeIndex, i)


for j in range(n):
      for i in range(n):
        if informationList[j][i] == 1:
          recur(j, i)
      for k in range(len(visited)):
        result[j][visited[k]] = 1
      visited = []

for j in range(n):
  for i in range(n):
    print(result[j][i],end=' ')
  print()