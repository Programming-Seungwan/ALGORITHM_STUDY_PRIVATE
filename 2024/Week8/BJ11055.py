from sys import stdin as s
s = open('./input.txt', 'rt')
n = int(s.readline().strip())
numberArray = list(map(int, s.readline().strip().split()))

dp = numberArray[:]
for i in range(n):
  for j in range(i):
    if numberArray[i] > numberArray[j] and dp[i] < dp[j] + numberArray[i]:
      dp[i] = dp[j] + numberArray[i] # 아래에서부터 끝까지 올라갈 가능성도 있는가?

# k 번째 숫자가 굉장히 크면 그 왼쪽의 왼만한 것들은 조건을 만족할 것이다. 따라서 이들 중에서 그냥 가장 큰 것을 기준으로 삼아야 한다. 즉, 내부 for 문은 처음부터 다 돌아야 한다고 볼 수 있다.
print(max(dp))