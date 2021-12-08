import numpy as np

with open('input.txt') as f:
    data = f.read().splitlines()

randNumbers = [int(num) for num in data[0].split(',')]

data = data[2:]
nrBoards = int((len(data) + 1) / 6.0)

board = np.zeros([5,5])

boardDicEx = {}
for nB in range(nrBoards):
    newBoard = board.copy()
    for i in range(5):
        newBoard[i,] = [int(s) for s in data[i].split() if s.isdigit()]

    boardDicEx[nB] = (newBoard, newBoard == -1, [False])
    del data[0:6]

def firstBoard(boardDic, randNums):
    bingo = False
    for num in randNums:
        for k,v in boardDic.items():
            curNumB = boardDic[k][0] == num
            idx = curNumB.nonzero()
            boardDic[k][1][idx] = True
            if ((boardDic[k][1].sum(axis = 0) == 5).any() or (boardDic[k][1].sum(axis = 1) == 5).any()):
                print("Bingo")
                bingo = True
                break
        if bingo:
            final = boardDic[k][0][boardDic[k][1] == False].sum() * num
            print('Part 1: ' + str(int(final)))
            return None

firstBoard(boardDic = boardDicEx, randNums = randNumbers)

def secondBoard(boardDic, randNums):
    for num in randNums:
        for k,v in boardDic.items():
            curNumB = boardDic[k][0] == num
            idx = curNumB.nonzero()
            boardDic[k][1][idx] = True
            if ((boardDic[k][1].sum(axis = 0) == 5).any()  or (boardDic[k][1].sum(axis = 1) == 5).any()):
                boardDic[k][2][0] = True
                if all(x == True for x in [v[2][0] for k,v in boardDic.items()]):
                    final = boardDic[k][0][boardDic[k][1] == False].sum() * num
                    print('Part 2: ' + str(int(final)))
                    return None

secondBoard(boardDic = boardDicEx, randNums = randNumbers)

