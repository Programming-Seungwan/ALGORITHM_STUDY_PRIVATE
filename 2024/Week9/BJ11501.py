from sys import stdin as s
s = open('./input.txt', 'rt')
n = int(s.readline().strip())

def greedy(stockList, benefit, endIndex): # 가장 큰 것까지 모두를 팔고 그 다음 남은 것들을 처리해야 함
  maxStockValue = max(stockList)
  maxStockValueIndex = stockList.index(maxStockValue)
  sum = 0
  for i in range(0, maxStockValueIndex):
    sum += (stockList[maxStockValueIndex] - stockList[i])
  benefit += sum
  greedy(stockList[maxStockValue + 1:], benefit, endIndex)
  if maxStockValue == endIndex:
    return benefit
  # 여기에서 함수의 재귀를 통해 benefit을 알맞게 늘린다
  return benefit

for _ in range(n):
  length = int(s.readline().strip())
  stockList = list(map(int, s.readline().strip().split()))
  benefitOne = 0
  result = greedy(stockList, benefitOne, length - 1)
  print(result)
  