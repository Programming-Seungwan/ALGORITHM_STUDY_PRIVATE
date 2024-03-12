# 2번쨰 동전의 가치부터는 계속해 나가면서 배수가 됨으로 부분 최적해가 전체 최적해를 구성한다는 것을 알 수 있다. 따라서 그리디 알고리즘을 사용할 수 있다.
from sys import stdin as s
#s = open('./input.txt', 'rt')
n, goal = list(map(int, s.readline().strip().split()))
coinList = []
for _ in range(n):
  coinList.append(int(s.readline().strip()))
result = 0
for i in range(n - 1, -1, -1):
  if coinList[i] <= goal:
    cointCount = goal // coinList[i]
    result += cointCount
    goal -= cointCount * coinList[i]
  else:
    continue

print(result)