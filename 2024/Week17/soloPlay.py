# 해당 배열의 모든 원소가 이미 체크되었는지를 확인하는 함수
def isListAllTrue(exampleList):
    for example in exampleList:
        if example == False:
            return False
    return True

def getFirstFalseIndex(exampleList):
    for i in range(len(exampleList)):
        if exampleList[i] == False:
            return i

def solution(cards):
    cardNum = len(cards)
    cardDic = {}
    for i in range(1, cardNum + 1):
        cardDic[i] = cards[i - 1]

    checkList = [False] * cardNum


    groupNumberList = [] # 해당 리스트는 각 그룹의 크기를 저장하는 자료구조
    tmpList = [] # 해당 리스트는 그룹을 임시로 저장하는 리스트임. 전체 순환이 끝나면 다시 0으로 바꿔줄 것임.
    nowCardIndex = 1
    while(not isListAllTrue(checkList)):
          nextCardIndex = cardDic[nowCardIndex]
          if checkList[nextCardIndex - 1] == True:
              checkList[nowCardIndex - 1] = True
              groupNumberList.append(len(tmpList))
              tmpList = []
              nowCardIndex = getFirstFalseIndex(checkList)

          else:
              tmpList.append(cardDic[nowCardIndex])
              checkList[nowCardIndex - 1] = True
              nowCardIndex = nextCardIndex
    # 임의로 하나를 뽑아서 그룹을 만들고, 한 그룹이 만들어지면 모두가 마무리되지 않는 이상, 계속 새로운 것을 뽑아서 새로운 그룹을 만들어야 함


    print(groupNumberList)
    # print(cardDic)

solution([8,6,3,7,2,5,1,4])