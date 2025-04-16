# 파스칼 케이스를 만드는 문제에 가까움
# 1. 쪼개는 과정이 필요함
# 2. 각 단어를 변환시키면 됨.
# 3. 단어의 시작이 숫자면 그 나머지는 그냥 죄다 소문자로 바꾸기
# 4. 단어의 시작이 영어면 첫번째만 대문자로 바꾸고 나머지는 소문자로 바꾸기
import re
# 단어를 보고 첫 글자를 통해 숫자로 시작하는지 영어로 시작하는지 판단하는 함수
# 단어를 변환시켜주는 함수가 필요
# 공백 문자가 연속해서 나올 수 있음. 여러 개의 공백을 감안하고 쪼개는 과정이 필요함.
# 공백은 계속해서 넣어두고 단어도 따로 넣어두기
# 특정 문자열에서 공백을 다 잘라버리기. 공백에 집중하기

def defineFirstChar(s):
  if s[0].isalpha() == True:
    return 'alpha'
  if s[0].isdigit() == True:
    return 'num'

def processWord(word, firstCharType):
  wordLength = len(word)
  returningWord = ""
  if firstCharType == 'num':
    returningWord += word[0]
    for i in range(1, wordLength):
      returningWord += word[i].lower()
  if firstCharType == 'alpha':
    returningWord += word[0].upper()
    for i in range(1, wordLength):
      returningWord += word[i].lower()

  return returningWord

def solution(s):
  totalList = list(filter(lambda x: x!='', re.split(r'(\s+)', s)))
  resultString = ""
  for word in totalList:
    if word[0] == ' ':
      resultString += word
    else:
      firstCharType = defineFirstChar(word)
      resultString += processWord(word, firstCharType)

  return resultString

# solution("3people unFollowed me")
# solution("for the last week")
