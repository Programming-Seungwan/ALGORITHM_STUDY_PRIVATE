def decideWhichGroup(number):
    number = str(number)
    if number in ['1', '4', '7']:
        return 'L'
    if number in ['3', '6', '9']:
        return 'R'
    else:
        return 'M' # 중간에 위치함을 의미함

def getNumberPosition(number):
    if number == 0:
        return [3, 1]
    if number == 1:
        return [0, 0]
    if number == 2:
        return [0, 1]
    if number == 3:
        return [0, 2]
    if number == 4:
        return [1, 0]
    if number == 5:
        return [1, 1]
    if number == 6:
        return [1, 2]
    if number == 7:
        return [2, 0]
    if number == 8:
        return [2, 1]
    if number == 9:
        return [2, 2]

def getDistance(numberPosition, handPosition):
    return abs((numberPosition[0] - handPosition[0]))  + abs((numberPosition[1] - handPosition[1]))

lhPosition = [3, 0]
rhPosition = [3, 2]

def solution(numbers, hand):
    answer = ''
    global lhPosition, rhPosition

    for num in numbers:
        groupResult = decideWhichGroup(num)
        numberPosition = getNumberPosition(num)
        # L이나 R로 나오면 그걸 이어 붙이기, 그리고 위치 갱신
        if groupResult == 'L':
            answer += 'L'
            lhPosition = numberPosition
            continue
        if groupResult == 'R':
            answer += 'R'
            rhPosition = numberPosition
            continue
        # M으로 나오면 거리를 계산해서 가까운 걸 이어붙이고 같으면 main hand를 이어 붙이기, 그리고 위치 갱신
        if groupResult == 'M':
            leftDistance = getDistance(lhPosition, numberPosition)
            rightDistance = getDistance(rhPosition, numberPosition)
            if (leftDistance < rightDistance):
                answer += 'L'
                lhPosition = numberPosition
            if (rightDistance < leftDistance):
                answer += 'R'
                rhPosition = numberPosition
            if (rightDistance == leftDistance):
                if (hand == 'right'):
                    answer += 'R'
                    rhPosition = numberPosition
                    continue
                if (hand == 'left'):
                    answer += 'L'
                    lhPosition = numberPosition
                    continue
    return answer

