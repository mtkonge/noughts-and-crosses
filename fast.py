import os
from TurnHandler import TurnHandler


def resetGame():
    if not os.path.exists("noughts-and-crosses.txt"):
        f = open('noughts-and-crosses.txt', 'x')
        f.close()
    if not os.path.exists("nonFormattedGame.txt"):
        f = open('nonFormattedGame.txt', 'x')
        f.close()
    with open("noughts-and-crosses.txt", "w") as f:
        with open("template.txt", "r") as t:
            f.write(t.read())
    with open("nonFormattedGame.txt", "w") as f:
        f.write("123456789") 

def printPositions(gameFile):
    with open(gameFile, "r") as f:
        print(f.read())

def recreateFile(file: str, replacement: str):
    with open(file, 'r') as f:
        content = f.read()
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


def playerTurn(gameFile: str, turnHandler: TurnHandler):
    userInput = input("Which position? ")
    if not validateInput(userInput):
        return
    with open(gameFile, "r+") as f:
        filecontent = f.read().replace(userInput, turnHandler.turn)
        recreateFile(gameFile, filecontent)
    turnHandler.switch()

def gameLoop(gameFile: str):
    resetGame()
    turnHandler = TurnHandler()
    while True:
        printPositions(gameFile)
        playerTurn(gameFile, turnHandler)
        
def main():

    gameLoop("nonFormattedGame.txt")

if __name__=="__main__":
    main()