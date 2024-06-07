def isNumber(inputString):
    if (inputString == "0" or inputString == "1" or inputString == "2" or inputString == "3" or inputString == "4" or inputString == "5" or inputString == "6" or inputString == "7" or inputString == "8" or inputString == "9"):
        return True
    else:
        return False

def isBonus(inputString):
    if (inputString == "S" or inputString == "D" or inputString == "T"):
        return True
    else:
        return False

def isOption(inputString):
    if (inputString == '*' or inputString == '#'):
        return True
    else:
        return False

def makeProcessedNumber(number, bonus):
    tmpprocessedNumber = 0
    if (bonus == 'S'):
        tmpprocessedNumber = number ** 1
    elif (bonus == 'D'):
        tmpprocessedNumber = number ** 2
    elif (bonus == 'T'):
        tmpprocessedNumber = number ** 3

    return tmpprocessedNumber


def solution(dartResult):
    dartDataList = []
    tmpString = ""
    answerList = []
    for i in range(len(dartResult)):
        if (i + 1< len(dartResult) and isNumber(dartResult[i]) and isNumber(dartResult[i + 1])):
            tmpString += dartResult[i]
            continue
        if(i + 1 < len(dartResult) and not isNumber(dartResult[i + 1])):
            tmpString += dartResult[i]
        else:
            tmpString += dartResult[i]
            dartDataList.append(tmpString)
            tmpString = ""

    for i in range(3):
        dartData = dartDataList[i] # 다트 데이터 하나에 해당함
        dartDataParsedList = []
        tmpToken = ""
        for j in range(len(dartData)):
            if (isBonus(dartData[j])):
                dartDataParsedList.append(tmpToken)
                dartDataParsedList.append(dartData[j])
            elif (isOption(dartData[j])):
                dartDataParsedList.append(dartData[j])
            else:
                tmpToken += dartData[j]

        if (len(dartDataParsedList) == 2):
            number = int(dartDataParsedList[0])
            bonus = dartDataParsedList[1]
            processedNumber = makeProcessedNumber(number, bonus)
            answerList.append(processedNumber)
        elif (len(dartDataParsedList) == 3):
            number = int(dartDataParsedList[0])
            bonus = dartDataParsedList[1]
            option = dartDataParsedList[2]
            processedNumber = makeProcessedNumber(number, bonus)
            if (option == '*'):
                if (i == 0):
                    processedNumber *= 2
                    answerList.append(processedNumber)
                else:
                    processedNumber *= 2
                    answerList.append(processedNumber)
                    answerList[i - 1] *= 2
            elif (option == '#'):
                processedNumber *= -1
                answerList.append(processedNumber)

    return sum(answerList)
