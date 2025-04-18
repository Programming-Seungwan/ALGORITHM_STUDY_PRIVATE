from sys import stdin as s
from itertools import permutations
s = open('./input.txt', 'rt')

N, M = map(int, s.readline().split())
maxBNum = N // M
totalCount = 0

def factorial(n):
  result = 1
  for i in range(1, n + 1):
    result = result * i
  return result


for i in range(maxBNum + 1):
  tmpList = [] # 숫자들을 넣어놓을 배열에 해당함
  #하나도 안 쓸때부터 최대치까지 M을 곱해서 뺀거만큼 1이 들어감
  oneCount = N - (i * M)
  for j in range(oneCount):
    tmpList.append(1)
  for k in range(i):
    tmpList.append(M)

  if oneCount == 0:
    totalCount += 1
    continue

  totalCount += len(list(permutations(tmpList))) // factorial(oneCount)

print(totalCount % 1000000007)