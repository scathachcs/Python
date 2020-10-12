class Bug:
    def __init__(self,initialPosition):
        self.Position=int(initialPosition)
        self.orientation=True
    def turn(self):
        self.orientation=not(self.orientation)
    def move(self):
        if self.orientation:
            self.Position+=1
        else:
            self.Position-=1
    def getPosition(self):
        return self.Position

def main():
    bug=Bug(0)
    for x in range(1,10,1):
        bug.move()
    bug.turn()
    bug.move()
    print(bug.getPosition())

if __name__ == "__main__":
    main()
