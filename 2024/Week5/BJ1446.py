from sys import stdin as s
s = open('./input.txt', 'rt')
routeNumber, endingPoint = list(map(int, s.readline().strip().split()))
routeList = [list(map(int, s.readline().strip().split())) for _ in range(routeNumber)]
# print(routeList)
routeRealList = []

for i in range(len(routeList)):
  startNode, endNode, length = routeList[i]
  if startNode <= endingPoint and endNode <= endingPoint:
    if length < (endNode - startNode):
      if startNode not in routeRealList:
        routeRealList.append(startNode)
      if endNode not in routeRealList:
        routeRealList.append(endNode)
if 0 not in routeRealList:
  routeRealList.append(0)
if endingPoint not in routeRealList:
  routeRealList.append(endingPoint)

routeRealList.sort()
routRealListLength = len(routeRealList)
twoDimensionList = [[0] * routRealListLength for _ in range(routRealListLength)]
for j in range(routRealListLength):
  for i in range(routRealListLength):
    twoDimensionList[j][i] = routeRealList[i] - routeRealList[j]

routeListLength = len(routeList)
# for i in range(routeListLength):
#   sP, eP, weight = routeList[i]
#   if (sP in routeRealList) and (eP in routeRealList):
