from table import table

class restaurant:
    def __init__(self, tables = 10):
        self.queue = []
        self.size = tables
        self.tables = [table(i+1) for i in range(self.size)]

    def printRestaurantInfo(self):
        for i in range(self.size):
            print("Table %d - Occupation: %s" % (self.tables[i].id, self.tables[i].occupied))

            if self.tables[i].occupied == True:
                partySize = 0

                for j in range(len(self.tables[i].seats)):
                    if self.tables[i].seats[j].occupied == True:
                        partySize += 1

                print("Table %d's Party Size %d" % (self.tables[i].id, partySize))

    def assignTable(self, partySize = 4):
        for i in range(self.size):
            if self.tables[i].occupied == False and self.tables[i].size >= partySize:
                self.tables[i].assignTable(partySize)
                break

    def unassignTable(self, id):
        for i in range(self.size):
            if self.tables[i].id == id:
                self.tables[i].unassignTable()
                break