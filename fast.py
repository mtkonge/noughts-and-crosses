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
        if row == '0':
            for i in range(3):
                print(i)
                for i in range(len(fileContent)):
                    if fileContent[i] == turnHandler.turn:
                        continue
                    if i == 2:
                        return True
                    return False



def checkWinConditions(gameFile: str, turnHandler: TurnHandler, lastPlay: str):
    with open(gameFile, "r") as f:
        fileContent = f.read()
        if lastPlay == '1':
            if fileContent[4] == turnHandler.turn:
                if fileContent[8] == turnHandler.turn:
                    return True
        switcher = {
        '1': 
            checkRow('0', fileContent, turnHandler)

        }
        return switcher.get(lastPlay, False)


        

def playerTurn(gameFile: str, turnHandler: TurnHandler):
    userInput = input("Which position (must be a number on board)? ")
    if not validateInput(userInput):
        return
    with open(gameFile, "r+") as f:
        filecontent = f.read().replace(userInput, turnHandler.turn)
        recreateFile(gameFile, filecontent)
    checkWinConditions(gameFile, turnHandler, userInput)
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