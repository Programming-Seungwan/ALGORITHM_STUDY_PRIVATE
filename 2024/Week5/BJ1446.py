from sys import stdin as s
s = open('./input.txt', 'rt')
routeNumber, endingPoint = list(map(int, s.readline().strip().split()))
routeList = [list(map(int, s.readline().strip().split())) for _ in range(routeNumber)]
nodeList = []
nodeList.append(endingPoint)
nodeList.append(0)
for i in range(len(routeList)):
  startNode, endNode, weight = routeList[i]
  if startNode <= endingPoint and endNode <= endingPoint:
    if startNode not in nodeList:
      nodeList.append(startNode)
    if endNode not in nodeList:
      nodeList.append(endNode)
nodeList.sort()
# [0, 50, 100, 110, 140, 150]
mapInfoDic = {}
for i in range(len(nodeList)):
  mapInfoDic[nodeList[i]] = {}
  for j in range(len(nodeList)):
    if i != j and i < j:
      mapInfoDic[nodeList[i]][nodeList[j]] = nodeList[j] - nodeList[i]

for i in range(len(routeList)):
  startNode, endNode, weight = routeList[i]
  if startNode in nodeList and endNode in nodeList:
    if mapInfoDic[startNode][endNode] > weight:
      mapInfoDic[startNode][endNode] = weight

visited = [False for _ in range(len(nodeList))]
visited[0] = True
for i in range(1, len(nodeList)):
  visitNode = nodeList[i]
  keyGroup = mapInfoDic[visitNode].keys()
  for key in keyGroup:
    if mapInfoDic[0][key] > mapInfoDic[0][visitNode] + mapInfoDic[visitNode][key]:
      mapInfoDic[0][key] = mapInfoDic[0][visitNode] + mapInfoDic[visitNode][key]

print(mapInfoDic[0][endingPoint])