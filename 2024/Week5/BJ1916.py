from sys import stdin as s
s = open('./input.txt', 'rt')
cityNum = int(s.readline().strip())
busNum = int(s.readline().strip())
busList = []
for _ in range(busNum):
  busList.append(list(map(int, s.readline().strip().split())))
startCity, endCity = list(map(int, s.readline().strip().split()))

twoDimensionDic = {}
for i in range(1, cityNum + 1):
  twoDimensionDic[i] = {}
  for j in range(1, cityNum + 1):
    if i != j:
      twoDimensionDic[i][j] = float('inf')
    if i == j:
      twoDimensionDic[i][j] = 0
for i in range(busNum):
  sCity, eCity, cost = busList[i]
  twoDimensionDic[sCity][eCity] = cost

visited = [False for _ in range(cityNum + 1)]
visited[0] = True
visited[startCity] = True

def getUnvisitedLowestCity(): # 아직 방문이 되지 않았고, 가장 비용이 낮은 도시를 찾아주는 함수
  tmpDic = twoDimensionDic[startCity]
  value = float('inf')
  index = 0
  for key in tmpDic:
    if visited[key] == False and tmpDic[key] < value:
      value = tmpDic[key]
      index = key
  return index

def ifAllCityVisited(): # 모든 도시가 방문이 완료되었는지를 체크하는 함수
  for  i in range(len(visited)):
    if visited[i] == False:
      return False
  return True

while not ifAllCityVisited():
  unvisitedLowestCity = getUnvisitedLowestCity()
  visited[unvisitedLowestCity] = True
  tmpUnvisitedDic = twoDimensionDic[unvisitedLowestCity]
  for key in tmpUnvisitedDic:
    if tmpUnvisitedDic[key] != float('inf'):
      if twoDimensionDic[startCity][key] > twoDimensionDic[startCity][unvisitedLowestCity] + twoDimensionDic[unvisitedLowestCity][key]:
        twoDimensionDic[startCity][key] = twoDimensionDic[startCity][unvisitedLowestCity] + twoDimensionDic[unvisitedLowestCity][key]
# print(visited)
# print(twoDimensionDic)
print(twoDimensionDic[startCity][endCity])