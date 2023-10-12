class Player :
    def __init__ (self , name , genre ):
        self.name = name
        self.genre = genre
        self.instruments = []
    def __str__ (self):
        '''The artist and their instruments '''
        return " Artist " + self.name + " plays " + ", ".join (self.instruments)
    def copy ( self ):
        p = Player (self.name , self.genre)
        p.instruments = list(self.instruments)
        return p
    def addInst (self , instrument ):
        self.instruments.append (instrument)
    def __eq__(self, other):
        a = list(self.instruments)
        b = list(other.instruments)
        a.sort()
        b.sort()
        return self.name == other.name and \
               self.genre == other.genre and \
               a == b
Meshell = Player (" Ndegeocello ", " rap")
Meshell . addInst (" bass ")
M2 = Meshell . copy ()
M2. addInst (" piano ")
print("Meshell object: ", Meshell)
print("M2 Object: ", M2)
p0 = Player("Attile Duck", "jazz")
p0.addInst("kazzo")
p0.addInst("guitar")
p1 = Player("Attile Duck", "jazz")
p1.addInst("guitar")
p1.addInst("kazzo")
print(p0 == p1)
    
