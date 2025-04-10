from sys import stdin as s
from itertools import combinations

s = open('./input.txt', "rt")

# n개를 1개부터 n개까지 뽑는 모든 조합을 싹다 구하고 더해서 정렬한뒤,  없으면 출력한다.
n = int(s.readline().strip())

dumbellList = list(map(int, s.readline().strip().split(' ')))
combinationSumList = []

for i in range(1, n + 1):
  tmpCombinationList = list(combinations(dumbellList, i))
  for tmpCombination in tmpCombinationList:
    combinationSumList.append(sum(tmpCombination))

combinationSumList.sort()

for i in range(0, len(combinationSumList)):
  diff = combinationSumList[i + 1] - combinationSumList[i]
  if (diff != 1 and diff != 0):
    print(combinationSumList[i] + 1)
    break
