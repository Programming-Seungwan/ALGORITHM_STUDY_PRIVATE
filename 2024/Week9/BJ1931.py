from sys import stdin as s
s = open('./input.txt', 'rt')
n = int(s.readline().strip())
meetingDictionary = {}
for _ in range(n):
  startTime, endTime = list(map(int, s.readline().strip().split()))
  if endTime not in meetingDictionary:
    meetingDictionary[endTime] = [startTime]
  else:
    meetingDictionary[endTime].append(startTime)

endTimeList = list(meetingDictionary.keys())
memo = [0 for _ in range(max(endTimeList) + 1)]
# 동일 시각에 시작해서 동일 시각에 끝나는 케이스를 처리해줘야 함
# for item in endTimeList:
#   maxStartTime = max(meetingDictionary[item]) # 해당 리스트에서 가장 큰 시간
#   tmpMemolist = memo[0:maxStartTime + 1]
#   memo[item] = max(tmpMemolist) + 1

for i in range(1, max(endTimeList) + 1):
  if i in endTimeList:
    maxStartTime = max(meetingDictionary[i])
    tmpMemoList = memo[0 : maxStartTime + 1]
    memo[i] = max(tmpMemoList) + 1
  else:
    memo[i] = max(memo[0:i])

  if i in meetingDictionary and i in meetingDictionary[i]:
    memo[i] += 1

print(max(memo))