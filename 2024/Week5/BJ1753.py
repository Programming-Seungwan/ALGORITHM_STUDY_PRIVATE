# vertex의 개수가 20000이기 때문에 floyd-warhall 알고리즘이 아닌, 다익스트라 알고리즘으로 풀어야 한다. 이는 visited를 통해서 연결된 것들만 차차 갱신해 나가기 때문이다.
# 어떠한 자료 구조에 담을 것인가?
from sys import stdin as s
s = open('./input.txt', 'rt')
vertexNum, edgeNum = list(map(int, s.readline().strip().split()))
startNode = int(s.readline().strip())
twoDimensionList = [[float('inf')] * (vertexNum + 1) for _ in range(vertexNum + 1)]
for i in range(edgeNum):
  sNode, eNode, weight = list(map(int, s.readline().strip().split()))
  twoDimensionList[sNode][eNode] = weight

visited = [False for _ in range(vertexNum + 1)]
visited[0] = True
visited[startNode] = True

def getCheapestUnvisitedNodeIndex(node):
  value = float('inf')
  index = -1
  for i in range(len(twoDimensionList[node])):
    if visited[i] == False and twoDimensionList[node][i] < value:
      index = i
      value = twoDimensionList[node][i]
  return index
# print(twoDimensionList)
while True:
  newNodeIndex = getCheapestUnvisitedNodeIndex(startNode)
  if newNodeIndex == -1:
    break
  for i in range(1, len(twoDimensionList[newNodeIndex])):
    if twoDimensionList[newNodeIndex][i] != float('inf'):
      if twoDimensionList[startNode][i] > twoDimensionList[startNode][newNodeIndex] + twoDimensionList[newNodeIndex][i]:
        twoDimensionList[startNode][i] = twoDimensionList[startNode][newNodeIndex] + twoDimensionList[newNodeIndex][i]
  visited[newNodeIndex] = True

twoDimensionList[startNode][startNode] = 0
for i in range(1, (vertexNum + 1)):
  if twoDimensionList[startNode][i] == float('inf'):
    print("INF")
  else:
    print(twoDimensionList[startNode][i])