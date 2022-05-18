from typing import Tuple


def main():
    positions: list[list] = [[1, ''], [2, ''], [3, ''], [4, ''], [5, ''], [6, ''], [7, ''], [8, ''], [9, ''] ]
    playerState = True
    while True:
        command = input("Which position? ")
        command = command.lower()
        for i in range(len(positions)):
            if int(command) == positions[i][0]:
                if playerState == True:
                    positions[i][1] = 'x'
                    
                else:
                    positions[i][1] = 'o'
                playerState = not playerState
            checkWinConditions(positions)
        
        print(positions)

def checkWinConditions(positions: list[list] ):
      for i in range(len(positions)):
            checkHorizontalWinConditions(positions, i)
            checkVerticalWinConditons(positions, i)
            checkCrossWinConditions(positions, i)

def checkHorizontalWinConditions(positions: list[list], i: int):
    if i == 0 or i == 3 or i == 6:
        if positions[i][1] == 'x':
            if positions[i+1][1] == 'x':
                if positions[i+2][1] == 'x':
                    print("player x won")
                    exit(0)
        if positions[i][1] == 'o':
            if positions[i+1][1] == 'o':
                if positions[i+2][1] == 'o':
                    print("player o won")
                    exit(0)

def checkVerticalWinConditons(positions: list[list], i: int):
    if i == 0 or i == 1 or i == 2:
        if positions[i][1] == 'x':
            if positions[i+3][1] == 'x':
                if positions[i+6][1] == 'x':
                    print("player x won")
                    exit(0)
        if positions[i][1] == 'o':
            if positions[i+3][1] == 'o':
                if positions[i+6][1] == 'o':
                    print("player o won")
                    exit(0)

def checkCrossWinConditions(positions: list[list], i: int):
    if i == 0:
        if positions[i][1] == 'x':
            if positions[i+4][1] == 'x':
                if positions[i+8][1] == 'x':
                    print("player x won")
                    exit(0)
        if positions[i][1] == 'o':
            if positions[i+4][1] == 'o':
                if positions[i+8][1] == 'o':
                    print("player o won")
                    exit(0)
    if i == 2:
        if positions[i][1] == 'x':
            if positions[i+2][1] == 'x':
                if positions[i+4][1] == 'x':
                    print("player x won")
                    exit(0)
        if positions[i][1] == 'o':
            if positions[i+2][1] == 'o':
                if positions[i+4][1] == 'o':
                    print("player o won")
                    exit(0)  
    

if __name__=="__main__":
    main()