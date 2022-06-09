import os
from TurnHandler import TurnHandler


def resetGame(gameFile: str):
    if not os.path.exists(gameFile):
        f = open(gameFile, 'x')
        f.close()   
    with open(gameFile, "w") as f:
        f.write("123456789") 

def recreateFile(file: str, replacement: str):
    os.remove(file)
    with open(file, 'w') as f:
        f.write(replacement)

def validateInput(userInput: str):
    if len(userInput) > 1 or userInput == "0":
        print("Invalid input")
        return False
    try:
        int(userInput)
    except:
        print("Invalid input")
        return False
    return True

def formatFile(gameFile: str):
    with open(gameFile, "r") as f:
        fileContent = f.read()
        return "|" + fileContent[0] + "|" + fileContent[1] + "|" + fileContent[2] + "|\n|" + fileContent[3] + "|" + fileContent[4] + "|" + fileContent[5] + "|\n|" + fileContent[6] + "|" + fileContent[7] + "|" + fileContent[8] + "|"

def checkRow(row: str, fileContent: str, turnHandler: TurnHandler):            
        if row == '1':
            startPosition = 3
        if row == '2':
            startPosition = 6
            print
        for i in range(3):
            print(fileContent[startPosition+i])
            for i in range(len(fileContent)):
                if fileContent[i+startPosition] == turnHandler:
                    continue
                if i == 2+startPosition:
                    return True
                return False

def checkColumn(col: str, fileContent: str, turnHandler: TurnHandler):
    return


def checkWinConditions(gameFile: str, turnHandler: TurnHandler, lastPlay: str):
    with open(gameFile, "r") as f:
        fileContent = f.read()
        print(lastPlay)
        if lastPlay == '1': 
            if checkRow('0', fileContent, turnHandler):
                return True
        elif lastPlay == '4':
            print("yes")
            if checkRow('1', fileContent, turnHandler):
                print("yesss")
                return True
        

def playerTurn(gameFile: str, turnHandler: TurnHandler):
    userInput = input("Which position (must be a number on board)? ")
    if not validateInput(userInput):
        return
    with open(gameFile, "r+") as f:
        filecontent = f.read().replace(userInput, turnHandler.turn)
        recreateFile(gameFile, filecontent)
    print(checkWinConditions(gameFile, turnHandler, userInput))
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