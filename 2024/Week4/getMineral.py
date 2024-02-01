import math

def breakMineral(pick, mineral):
    if pick == 'diamond':
        return 1
    if pick == 'iron':
        if mineral == 'diamond':
            return 5
        else:
            return 1
    if pick == 'stone':
        if mineral == 'diamond':
            return 25
        if mineral == 'iron':
            return 5
        if mineral == 'stone':
            return 1

combinationList = []
picksList = ['diamond', 'iron', 'stone']

def solution(picks, minerals):
    picksLength = sum(picks)
    mineralsLength = len(minerals)
    upAdJustDivideResult = math.ceil(mineralsLength / 5)
    combinationNumber = upAdJustDivideResult if upAdJustDivideResult <= picksLength else picksLength

    tmpCombination = []
    def getPickCombination(cnt):
        if cnt == combinationNumber:
            combinationList.append(tmpCombination)
            return

        for i in range(len(picks)):
            if picks[i] != 0:
                tmpCombination.append(picksList[i])
                
                picks[i] = picks[i] - 1
                getPickCombination(cnt + 1)
                tmpCombination.pop()
                picks[i] = picks[i] + 1

    getPickCombination(0)

    print(combinationList)



picks = [1, 3, 2]
minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
solution(picks, minerals)


# picks = [0, 1, 1]
# minerals = ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]
# print(solution(picks, minerals))

# 미네랄 개수를 곡괭이 개수로 나눈다 => 올려치기를 하고 이것이 곡괭이 개수보다 많으면 조합의 개수는 곡괭이 수이고 곡괭이 개수보다 작거나 같다면 올려치기한 값이 조합의 개수이다. 
# 갯수가 허락하는 한에서 뽑아서 순서를 배치한다 => 중복 순열
# 각 케이스의 피로도를 계산한다. 그 중에서 가장 작은 피로도를 출력하는 것
