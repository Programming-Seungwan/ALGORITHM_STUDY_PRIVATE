# 배열에 모두 저장한다. 들어갔는지 카운트를 리턴해주는 함수가 필요하다.
# 특정 인물의 순위가 정해졌다면 이를 이용해서 다른 인물들의 것도 갱신해준다

def solution(n, results):
  visited = [0] * (n + 1)
  result = 0

  # 해당 행, 즉 사용자가 다른 사람들과 관계를 n-1번 만큼 맺었는지를 판별해주는 함수
  def isNMinusOne(list):
    count = 0
    for i in range(1, n + 1):
      if list[i] == 1 or list[i] == -1:
        count += 1
    if count == (n - 1):
      return True
    else:
      return False

  twoDimensionList = [[float('inf')] * (n + 1) for _ in range(n + 1)]
  for j in range(n + 1):
    for i in range(n + 1):
      if i == 0 or j == 0:
        twoDimensionList[j][i] = 0
  for i in range(len(results)):
    winner, loser = results[i]
    twoDimensionList[winner][loser] = 1
    twoDimensionList[loser][winner] = -1

  def updateOthers(list):
      winList = []
      loseList = []
      for i in range(1, n + 1):
        if list[i] == 1:
          winList.append(i)
        if list[i] == -1:
          loseList.append(i)
      for j in range(len(winList)):
        for i in range(len(loseList)):
          win = winList[j]
          lose = loseList[i]
          twoDimensionList[win][lose] = -1
      for j in range(len(loseList)):
        for i in range(len(winList)):
          lose = loseList[j]
          win = winList[i]
          twoDimensionList[lose][win] = 1

  def isCandidateLive():
    for i in range(1, n + 1):
      if visited[i] == 0 and isNMinusOne(twoDimensionList[i]):
        return True
    return False

  while isCandidateLive():
    for i in range(1, n + 1):
      if visited[i] == 0 and isNMinusOne(twoDimensionList[i]):
        visited[i] = 1
        updateOthers(twoDimensionList[i])
        result += 1
        break
  # print(twoDimensionList)
  return result


solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])