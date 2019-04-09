from seat import seat

class table:
    def __init__(self, id, size = 4):
        self.id = id
        self.size = size
        self.seats = [seat() for i in range(size)]
        self.occupied = False

    def printAllSeatsStatus(self):
        for i in range(self.size):
            print("Seat #%d - Occupied : %s" % (i+1 , self.seats[i].occupied))

    def assignTable(self, party_size):
        if party_size > self.size:
            print("Table too small for party")
            return -1 # -1 is error detector
        
        for i in range(party_size):
            self.seats[i].changeOccupied()

        self.occupied = True

    def unassignTable(self):
        if self.seats[0].occupied == True:
            self.seats[0].changeOccupied()
        else:
            self.occupied = False

        try:
            for i in range(self.size):
                if self.seats[i+1].occupied == True:
                    self.seats[i+1].changeOccupied()
                else:
                    break
        except IndexError:
            pass

        self.occupied = False