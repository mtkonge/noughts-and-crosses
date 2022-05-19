class TurnHandler:
    def __init__(self):
        self.turn = 'x'

    def switch(self):
        if self.turn == 'x':
            self.turn = 'o'
        else:
            self.turn = 'x' 

