def getUpperNumberByDiv(num, divider): # 특정 숫자의 뭐로 나눔
    realDivider = 10 ** divider
    quotient = num // realDivider
    remain = num % realDivider
    if (remain == 0):
        return num
    else:
        return (quotient + 1) * realDivider



def getMinusCount(number):
    total = 0
    length = len(str(number)) - 1
    for i in range(length, -1 , -1):
        quot = number // (10 ** i)
        number -= quot * (10 ** i)
        total += quot
    return total


def solution(storey):
    result = [] # 각 케이스들을 담을 자료 배열
    storyLength = len(str(storey))
    result.append(getMinusCount(storey)) # 그냥 내리는 케이스를 고르기
    for i in range(1,storyLength):
        revisedStory = getUpperNumberByDiv(storey, i)
        print(revisedStory)
        diff = revisedStory - storey
        tmpResult = getMinusCount(revisedStory) + getMinusCount(diff)
        result.append(tmpResult)

    return min(result)

# print(solution(16))
print(solution(2554))
