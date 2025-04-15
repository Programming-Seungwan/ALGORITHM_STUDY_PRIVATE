from sys import stdin as s
s = open('./input.txt', 'rt')

n = int(s.readline().strip())

wineList = [0] + [int(s.readline().strip()) for _ in range(n)]
memo = [0 for _ in range(n + 1)]
memo[1] = wineList[1]
if n == 1:
  print(memo[1])
  exit(0)
memo[2] = memo[1] + wineList[2]

if n > 2:
  for i in range(3, n + 1):
    memo[i] = max(memo[i -2] + wineList[i], memo[i - 3] + wineList[i - 1] + wineList[i], memo[i -1])

print(max(memo))
