def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]
    if len(sticker) == 2:
        return max(sticker[0], sticker[1])

    totalLength = len(sticker)
    memoOne = [0 for _ in range(totalLength - 1)]
    memoTwo = [0 for _ in range(totalLength)]
    # 첫번째 칸 스티커를 뽑았을 경우
    for i in range(2, totalLength - 1):
        if i == 2:
            memoOne[i] = sticker[i]
        else:
            memoOne[i] = max(memoOne[i - 2] + sticker[i], memoOne[i - 1])
    # 첫 번째 칸 스티커를 뽑지 않았을 경우
    for i in range(1, totalLength):
        if i == 1:
            memoTwo[i] =sticker[i]
        else:
            memoTwo[i] = max(memoTwo[i - 2] + sticker[i], memoTwo[i - 1])
    memoOneLargest = max(memoOne) + sticker[0]
    memotwoLargest = max(memoTwo)
    return max(memotwoLargest, memoOneLargest)