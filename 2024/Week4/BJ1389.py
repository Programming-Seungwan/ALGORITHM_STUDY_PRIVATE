from sys import stdin as s
from collections import deque
s = open('./input.txt', 'rt')
userNum, relationShipNum = list(map(int, s.readline().strip().split()))
relationDic = {}
visitedList = [[False] * userNum for _ in range(userNum + 1)] # 0 인덱스는 따로 사용하지 않는다
count = 0
for i in range(1, userNum + 1):
  relationDic[i] = []
for i in range(relationShipNum):
  firstNode, secondNode = list(map(int, s.readline().strip().split()))
  relationDic[firstNode].append(secondNode)
  relationDic[secondNode].append(firstNode)

def recur(originUser, newUser):
  global count
  queue = deque()

  

# print(relationDic)
# print(visitedList)
