import itertools

def makeEntry(myList):
    returnList = []
    for st in myList:
        for stringChar in st:
            if stringChar in returnList:
                continue
            else:
                returnList.append(stringChar)
    return returnList

def ifMenuContaionCombo(menu, combo):
    for comboChar in combo:
        if comboChar in menu:
            continue
        else:
            return False
    return True

def solution(orders, course):
    # 조합들을 만들고, 해당 조합에 해당하는 사람이 2명이면 answer에 투입
    answer = []
    menuList = makeEntry(orders) # 모든 음식들을 여기에 중복 없이 모아놓음

    prevMaxCount = 0
    for i in course:
        combinations = itertools.combinations(menuList, i)
        for combo in combinations:
            comboString = ''.join(combo) # 조합으로 뽑혀져 나온 것
            count = 0
            for menu in orders:
                if (ifMenuContaionCombo(menu, comboString)):
                    count += 1
            if (count >= 2 & count >= prevMaxCount):
                answer.append(comboString)
                prevMaxCount = count
            count = 0
        prevMaxCount = 0
    return answer