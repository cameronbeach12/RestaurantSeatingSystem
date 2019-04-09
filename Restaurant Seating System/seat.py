class seat:
    def __init__(self):
        self.occupied = False

    def changeOccupied(self):
        if self.occupied == True:
            self.occupied = False
        else:
            self.occupied = True