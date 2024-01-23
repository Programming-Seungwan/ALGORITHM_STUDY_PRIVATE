# 부분 수열의 정의는 연속된 것이어야 한다
# 백트래킹에서는 스택에서 뺴주는 것은 check도 풀어주는 것이다.

from sys import stdin as s
import sys
sys.setrecursionlimit(10000)
s = open('./input.txt', 'rt')

N, S = list(map(int, s.readline().strip().split(' ')))

fullNumbers = list(map(int, s.readline().strip().split(' ')))
fullNumbersLength = len(fullNumbers)
res = []
check = [False] * (fullNumbersLength + 1)
count = 0



# 해당함수는 res의 값이 s와 같으면 전체 카운트를 늘린다
def recur():
  global count
  if sum(res) == S:
    count += 1
    return

  for j in range(fullNumbersLength):
    res.append(fullNumbers[j])
    check[j] = True
    recur()
    check[j] = False
    res.pop()

recur()

print(count)
# 해당 문제는 틀린 풀이