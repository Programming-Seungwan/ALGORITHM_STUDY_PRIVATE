from sys import stdin as s
s = open('./input.txt', 'rt')
n = int(s.readline())
wineList = [0]
for _ in range(n):
  wineList.append(int(s.readline()))
memo = [0 for _ in range(n + 1)]

memo[1] = wineList[1]
if n >=2:
  memo[2] = wineList[1] + wineList[2]

if n >= 3:
  for i in range(3, n + 1): # i번째 잔을 마시는데 i-1을 마시는 경우와 마시지 않는 경우, 그리고 i번째 잔 자체를 마시지 않는 경우
    memo[i] = max(memo[i - 3] + wineList[i - 1] + wineList[i], memo[i - 2] + wineList[i], memo[i - 1])




print(memo[n])