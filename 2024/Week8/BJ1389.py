from sys import stdin as s
#s = open('./input.txt', 'rt')
userNum, relationshipNum = list(map(int, s.readline().strip().split()))
relationshipDic = {}
for i in range(1, userNum + 1):
  relationshipDic[i] = []
for _ in range(relationshipNum):
  userOne, userTwo = list(map(int, s.readline().strip().split()))
  if userOne not in relationshipDic[userTwo]:
    relationshipDic[userTwo].append(userOne)
  if userTwo not in relationshipDic[userOne]:
    relationshipDic[userOne].append(userTwo)

relationDoubleDemensionList = [[float('inf')] * (userNum + 1) for _ in range(userNum + 1)] # 계속해서 갱신해나갈 것에 해당.
for j in range(userNum + 1): # 일단 채워지지 않은 것들은 무한대로 설정해놓는다
  for i in range(userNum + 1):
    if j == 0 or i == 0:
      relationDoubleDemensionList[j][i] = 0
    if j == i:
      relationDoubleDemensionList[j][i] = 0

for i in range(1, userNum + 1):
  for j in range(len(relationshipDic[i])):
    relationDoubleDemensionList[i][relationshipDic[i][j]] = 1

for k in range(1, userNum + 1):
  for j in range(1, userNum + 1):
    for i in range(1, userNum + 1):
      beforeValue = relationDoubleDemensionList[j][i]
      tmpValue = relationDoubleDemensionList[j][k] + relationDoubleDemensionList[k][i]
      if tmpValue < beforeValue:
        relationDoubleDemensionList[j][i] = tmpValue

baconResult = [0 for _ in range(userNum + 1)]
for i in range(1, userNum + 1):
  baconResult[i] = sum(relationDoubleDemensionList[i])

resultIndex = 1
resultSum = baconResult[1]
for i in range(2, userNum + 1):
  if baconResult[i] < resultSum:
    resultIndex = i
    resultSum = baconResult[i]

print(resultIndex) # 플로이드 와샬 알고리즘을 이용하여 케빈 - 베이컨 문제를 풀이