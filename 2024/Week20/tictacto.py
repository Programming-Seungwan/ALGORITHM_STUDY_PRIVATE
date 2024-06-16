def isGameOver(board): # 연속된 3개가 있는지를 검사하기
    firstWon = False
    secondWon = False
    for i in range(3):
        if board[i][0] == 'O' and board[i][1] == 'O' and board[i][2] == 'O':
            firstWon = True
        if board[i][0] == 'X' and board[i][1] == 'X' and board[i][2] == 'X':
            secondWon = True
        if board[0][i] == 'O' and board[1][i] == 'O' and board[2][i] == 'O':
            firstWon = True
        if board[0][i] == 'X' and board[1][i] == 'X' and board[2][i] == 'X':
            secondWon = True
    if (board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O'):
        firstWon = True
    if (board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X'):
        secondWon = True
    if (board[2][0] == 'O' and board[1][1] == 'O' and board[0][2] == 'O'):
        firstWon = True
    if (board[2][0] == 'X' and board[1][1] == 'X' and board[0][2] == 'X'):
        secondWon = True

    if ((firstWon == False) and (secondWon == False)):
        return 0 # 둘다 경기를 끝내지 못했을 떄
    elif ((firstWon == True) and (secondWon == False)):
        return 1 # 선공이 이겼을 때
    elif ((firstWon == False) and (secondWon == True)):
        return 2 # 후공이 이겼을 때
    else:
        return 3 # 선공 후공이 모두 이겼을 때 -> 이떄는 일어날 수 없는 케이스이므로 본 함수에서 return 0으로 처리

def solution(board):
    tttBoard = [[b[0], b[1], b[2]] for b in board]
    firstCount = 0
    secondCount = 0
    for i in range(3):
        for j in range(3):
            if tttBoard[i][j] == 'O':
                firstCount += 1
            elif (tttBoard[i][j] == 'X'):
                secondCount += 1

    result = isGameOver(tttBoard)
    if (result == 1): # 선공이 이겼을 때
        if ((firstCount - secondCount) == 1):
            return 1
        else:
            return 0
    elif (result == 2):
        if (firstCount == secondCount):
            return 1
        else:
            return 0
    elif (result == 3):
        return 0
    elif (result == 0):
        gap = firstCount - secondCount
        if (gap == 1 or gap == 0):
            return 1
        else:
            return 0

    return 1

print(solution(["O.X", ".O.", "..X"]))
print(solution(["OOO", "...", "XXX"]))
print(solution(["...", ".X.", "..."]))
print(solution(["...", "...", "..."]))