from sys import stdin as s
n = int(s.readline().strip())
guitarList = [s.readline().strip() for _ in range(n)]

# 길이가 다르면 짧은 거 먼저
# 길이가 같으면 숫자합이 더 작은 거 먼저
# 사전순으로 비교 숫자가 알파벳보다 작다
def numberSum(guitar):
  guitarLen = len(guitar)
  result = 0
  for i in range(guitarLen):
    if guitar[i].isalpha():
      continue
    if guitar[i].isdigit():
      result += int(guitar[i])
  return result

guitarList.sort(key= lambda x : (len(x), numberSum(x), x))
for i in range(n):
   print(guitarList[i])