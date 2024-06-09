sample = ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"]

sampleData = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

def makeWatingMatrix(mtx): # 해당 2차원 배열을 반환함
    returningMtx = [[] for _ in range(5)]
    for i in range(5):
        for j in range(5):
            returningMtx[i].append(mtx[i][j])
    return returningMtx


def calDistance(oneX, oneY, twoX, twoY):
    return abs(oneX - twoX) + abs(oneY - twoY)

def checkIsOkayMatrix(leftX, leftY, rightX, rightY, mtx): # 2 바 2로 있을 때 파티션들이 있는지를 검사하는 함수
    if (mtx[leftX][leftY + 1] == 'X' and mtx[rightX - 1][rightY] == 'X'):
        return True
    else:
        return False

def checkIsGood(tmpPeopleList, mtx):
    for i in range(len(tmpPeopleList)):
            personOneX, personOneY = tmpPeopleList[i]
            for j in range(i + 1, len(tmpPeopleList)):
                personTwoX, personTwoY = tmpPeopleList[j]
                if (calDistance(personOneX, personOneY, personTwoX, personTwoY) > 2):
                    continue
                elif (calDistance(personOneX, personOneY, personTwoX, personTwoY) == 2):
                    if(personOneX < personTwoX): # 1사람이 더 왼쪽에 있는 경우
                        if(checkIsOkayMatrix(personOneX, personOneY, personTwoX, personTwoY,mtx) == True):
                            continue
                        else:
                            return False
                    else:
                        if(checkIsOkayMatrix(personTwoX, personTwoY, personOneX, personOneY,mtx) == True):
                            continue
                        else:
                            return False
                elif (calDistance(personOneX, personOneY, personTwoX, personTwoY) == 2):
                    if (personOneX == personTwoX):
                        if (mtx[personOneX][personOneY + 1] == 'X'):
                            continue
                        else:
                            return False
                    else:
                        if (mtx[personOneX + 1][personOneY] == 'X'):
                            continue
                        else:
                            return False

    return True

def solution(places):
    answer = []

    for p in places:
        peopleList = []
        tmpMtx = makeWatingMatrix(p)
        for i in range(5):
            for j in range(5):
                if tmpMtx[i][j] == 'P':
                    peopleList.append([i, j])
        print(peopleList)

        if (len(peopleList) == 0 or len(peopleList) == 1):
            answer.append(1)
            continue

        result = checkIsGood(peopleList, tmpMtx)
        if result == True:
            answer.append(1)
        else:
            answer.append(0)

    return answer

print(solution(sampleData))