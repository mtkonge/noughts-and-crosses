

def printPositions():
    with open("noughts-and-crosses.txt", "r") as f:
        print(f.read())

def gameLoop(positions: list[list]):
    while True:
        printPositions()
        userInput = input("Which position? ")
        userInput = userInput.lower()
        if 
def main():
    positions: list[list] = [[1, ''], [2, ''], [3, ''], [4, ''], [5, ''], [6, ''], [7, ''], [8, ''], [9, '']]
    gameLoop(positions)

if __name__=="__main__":
    main()