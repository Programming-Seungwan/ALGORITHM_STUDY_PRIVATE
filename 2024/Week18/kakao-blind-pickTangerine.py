# 딕셔너리에서 가장 개수가 많은 사이즈를 반환하는 함수
def mostManySize(dic):
    dicKeyList = list(dic.keys())

    returnValue = dicKeyList[0]
    for dicKey in dicKeyList:
        if dic[returnValue] < dic[dicKey]:
            returnValue = dicKey
    return returnValue



def solution(k, tangerine):
    count = k
    answer = 0
    tangerineDic = {}
    tangerineDicKeyList = list(set(tangerine))
    for tangerinDicKey in tangerineDicKeyList:
        tangerineDic[tangerinDicKey] = 0
    for tg in tangerine:
        tangerineDic[tg] += 1

    while (count > 0):
        mostValueCountKey = mostManySize(tangerineDic)
        if (tangerineDic[mostValueCountKey] <= count):
            count -= tangerineDic[mostValueCountKey]
            tangerineDic[mostValueCountKey] = 0
            answer += 1
        else:
            count = 0
            tangerineDic[mostValueCountKey] -= count
            answer += 1

    return answer

print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]))


## 정답 풀이
def solution(k, tangerine):
    answer = 0

    d = {}
    for i in tangerine:
        if (i in d):
            d[i] += 1
        else:
            d[i] = 1

    d = sorted(d.items(), key = lambda x: x[1], reverse = True)

    for i in d:
        k -= i[1]
        answer += 1
        if (k <= 0):
            break

    return answer