# 문제 풀이 프로세스
# 1. 입력 변수를 설정하고, 해당 변수는 처리할 때마다 갱신된다.
# 2. 새로 입력을 받을 때, 최대한 긴 것이 사전에 있는지를 확인하고 없다면 사전에 추가한다.
# 3. 길이가 1자리인 것은 무조건 사전에 있어야함을 보장해야 하므로 미리 만들어놓는 것이다.
# 4. 어떻게 해당 인덱스를 순환할지? 우선 특정 입력이 리스트에 있는지를 매번 확인해야한다.

wordDictionaryList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'KA']

def getMaxWidthString(tmpMsg, idx):
  tmpIndex = idx
  tmpString = tmpMsg[tmpIndex]
  while True:
    if ((tmpString + tmpMsg[tmpIndex + 1]) in wordDictionaryList):
      tmpString += tmpMsg[tmpIndex + 1]
      tmpIndex += 1
    else:
      break
  return [tmpString, tmpIndex] # 가장 긴 문자열과 해당 문자열의 마지막 인덱스를 반환

# print(getMaxWidthString('KAKAO', 2))


def findIndexInDictionary(ch, dictionary): # 특정 요소가 딕셔너리에서 어느 인덱스에 위치했는지를 반환하는 함수
  for i in range(len(dictionary)):
    if (ch == dictionary[i]):
      return i

# print(findIndexInDictionary('C', wordDictionaryList))


def solution(msg):
  answer = []
  msgLength = len(msg)

  idx = 0
  while (idx < msgLength - 1):
    maxString, maxStringIndex = getMaxWidthString(msg, idx)
    # print(maxString, maxStringIndex)
    answer.append(findIndexInDictionary(maxString, wordDictionaryList) + 1)
    idx = maxStringIndex + 1


  return answer

print(solution('KAKAO'))

print(solution('TOBEORNOTTOBEORTOBEORNO'))