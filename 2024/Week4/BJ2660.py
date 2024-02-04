from sys import stdin as s
#s = open('./input.txt', 'rt')
userNum = int(s.readline().strip())
relationShipDic = {}
for i in range(1, userNum + 1):
  relationShipDic[i] = []
# 회원 간의 관계를 딕셔너리에 넣어줌
while True:
  userOne, userTwo = list(map(int, s.readline().strip().split()))
  if userOne == -1 and userTwo == -1:
    break
  relationShipDic[userOne].append(userTwo)
  relationShipDic[userTwo].append(userOne)

# 가장 가까운 관계로 특정 인물과의 relationship을 정의하기 때문에 다익스트라, 혹은 플로이드 와샬 최단거리 알고리즘을 사용해야 한다
# 아이디어 : 다익스트라 알고리즘을 통해서 각 회원이 가장 먼 사이의 사람과 몇 다리 사이인지를 구한다. 그 후에 가장 인싸를 회장으로 선출한다.
# 회장 후보의 점수, 후보 수를 첫 줄에 출력
# 회장 후보의 리스트들을 나열
relationDoubleDemensionList = [[float('inf')] * (userNum + 1) for _ in range(userNum + 1)] # 계속해서 갱신해나갈 것에 해당
for j in range(userNum + 1):
  for i in range(userNum + 1):
    if j == 0 or i == 0:
      relationDoubleDemensionList[j][i] = 0
    if j == i:
      relationDoubleDemensionList[j][i] = 0
for i in range(1, userNum + 1):
  for j in range(len(relationShipDic[i])):
    relationDoubleDemensionList[i][relationShipDic[i][j]] = 1

# print(relationDoubleDemensionList)
def floydWarshall():
  for k in range(1, userNum + 1): # 거쳐 가는 노드 k
    for j in range(1, userNum + 1): # 출발노드 j
      for i in range(1, userNum + 1): # 도착노드 i
        if k != j and k != i and i != j:
          beforeValue = relationDoubleDemensionList[j][i]
          tmpValue = relationDoubleDemensionList[j][k] + relationDoubleDemensionList[k][i]
          if tmpValue < beforeValue:
            relationDoubleDemensionList[j][i] = tmpValue

floydWarshall()
result = [0 for _ in range(userNum + 1)]

for i in range(1, userNum + 1):
  result[i] = max(relationDoubleDemensionList[i])

bossGrade = float('inf')
bossMembers = []
for i in range(1, userNum + 1):
  if result[i] < bossGrade:
    bossGrade = result[i]
for i in range(1, userNum + 1):
  if result[i] == bossGrade:
    bossMembers.append(i)
print(bossGrade, len(bossMembers))
bossCandidateMembers = ' '.join(str(mem) for mem in bossMembers)
print(bossCandidateMembers)