from sys import stdin as s
s = open('./input.txt', 'rt')

T = int(s.readline().strip())
def dp(n, p):
  memo = [0 for _ in range(n + 1)] # 기록해놓을 자료구조에 해당
  for i in range(1, n + 1):
    comparingValue = memo[i - 1] + i
    if (comparingValue != p):
      memo[i] = comparingValue
    else:
      memo[i] = memo[i - 1]
  print(memo[n])

for _ in range(T):
  N, P = list(map(int, s.readline().strip().split(' ')))
  dp(N, P)






