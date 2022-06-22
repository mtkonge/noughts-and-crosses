import os
from TurnHandler import TurnHandler


def resetGame(gameFile: str):
    if not os.path.exists(gameFile):
        f = open(gameFile, 'x')
        f.close()   
    with open(gameFile, "w") as f:
        f.write("123456789") 

def recreateFile(gameFile: str, replacement: str):
    os.remove(gameFile)
    with open(gameFile, 'w') as f:
        f.write(replacement)

def validateInput(userInput: str, gameFile):
    if len(userInput) > 1 or userInput == "0":
        print("Invalid input")
        return False
    try:
        int(userInput)
    except:
        print("Invalid input")
        return False
    with open(gameFile, 'r') as f:
        fileContent = f.read()
        if not userInput == fileContent[int(userInput)-1]:
            print("That position is taken")
            return False 
    return True

def formatFile(gameFile: str):
    with open(gameFile, "r") as f:
        fileContent = f.read()
        return "|" + fileContent[0] + "|" + fileContent[1] + "|" + fileContent[2] + "|\n|" + fileContent[3] + "|" + fileContent[4] + "|" + fileContent[5] + "|\n|" + fileContent[6] + "|" + fileContent[7] + "|" + fileContent[8] + "|"

def checkRow(row: str, fileContent: str, turnHandler: TurnHandler) -> bool:            
    startPosition = 0
    if row == '1':
        startPosition = 3
    if row == '2':
        startPosition = 6
    for i in range(3):
        if i == 2 and fileContent[startPosition+i] == turnHandler.turn:
            return True
        if fileContent[startPosition+i] == turnHandler.turn:
            continue
        return False

def checkColumn(col: str, fileContent: str, turnHandler: TurnHandler):
    startPosition = 0
    if col == '1':
        startPosition = 1
    if col == '2':
        startPosition = 2
    for i in range(3):
        if i == 2 and fileContent[startPosition+i*3] == turnHandler.turn:
            return True
        if fileContent[startPosition+i*3] == turnHandler.turn:
            continue
        return False

def checkVerticalAndHorizontal(row: str, col: str, fileContent: str, turnHandler: TurnHandler):
    if checkRow(row, fileContent, turnHandler) or checkColumn(col, fileContent, turnHandler):
        return True

def checkCrossDown(fileContent: str, turnHandler: TurnHandler):
    for i in range(3):
        if i == 2 and fileContent[i*4] == turnHandler.turn:
            return True
        if fileContent[i*4] == turnHandler.turn:
            continue
        return False

def checkCrossUp(fileContent: str, turnHandler: TurnHandler):
    for i in range(3):
        if i == 2 and fileContent[i*2+2] == turnHandler.turn:
            return True
        if fileContent[i*2+2] == turnHandler.turn:
            continue
        return False

def checkWinConditions(gameFile: str, turnHandler: TurnHandler, lastPlay: str):
    with open(gameFile, "r") as f:
        fileContent = f.read()
        if lastPlay == '1':
            if checkVerticalAndHorizontal('0', '0', fileContent, turnHandler) or checkCrossDown(fileContent, turnHandler):
                return True
        elif lastPlay == '2':
            if checkVerticalAndHorizontal('0', '1', fileContent, turnHandler):
                return True
        elif lastPlay == '3':
            if checkVerticalAndHorizontal('0', '2', fileContent, turnHandler) or checkCrossUp(fileContent, turnHandler):
                return True    
        elif lastPlay == '4':
            if checkVerticalAndHorizontal('1', '0', fileContent, turnHandler):
                return True
        elif lastPlay == '5':
            if checkVerticalAndHorizontal('1', '1', fileContent, turnHandler) or checkCrossDown(fileContent, turnHandler) or checkCrossUp(fileContent, turnHandler):
                return True
        elif lastPlay == '6':
            if checkVerticalAndHorizontal('1', '2', fileContent, turnHandler):
                return True
        elif lastPlay == '7':
            if checkVerticalAndHorizontal('2', '0', fileContent, turnHandler) or checkCrossUp(fileContent, turnHandler):
                return True
        elif lastPlay == '8':
            if checkVerticalAndHorizontal('2', '1', fileContent, turnHandler):
                return True
        elif lastPlay == '9':
            if checkVerticalAndHorizontal('2', '2', fileContent, turnHandler) or checkCrossDown(fileContent, turnHandler):
                return True
        return False
        
        

def playerTurn(gameFile: str, turnHandler: TurnHandler):
    userInput = input("Which position (must be a number on board)? ")
    if not validateInput(userInput, gameFile):
        return
    with open(gameFile, "r+") as f:
        filecontent = f.read().replace(userInput, turnHandler.turn)
    recreateFile(gameFile, filecontent)
    if checkWinConditions(gameFile, turnHandler, userInput):
        print("Player " + turnHandler.turn + " won")
        exit(0)
    turnHandler.switch()
    

def gameLoop(gameFile: str):
    resetGame(gameFile)
    turnHandler = TurnHandler()
    while True:
        print(formatFile(gameFile))
        playerTurn(gameFile, turnHandler)
        
def main():
    gameLoop("nonFormattedGame.txt")

if __name__=="__main__":
    main()