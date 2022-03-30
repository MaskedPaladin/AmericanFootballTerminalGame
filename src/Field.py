import Canvas as C

class Field:
    def __init__(self, maxSizeX, maxSizeY):
        self.maxSizeX = maxSizeX
        self.maxSizeY = maxSizeY

        self.portions = maxSizeX/12

        self.lineCoordinates = []
        self.scrimmageLine = 50
        for x in range(self.maxSizeX):    
            if x%9 == 0:
                self.lineCoordinates.append(int(x+1+self.portions))
        self.canvas = C.Canvas(self.maxSizeX, self.maxSizeY)

        for x in range(self.maxSizeX):
            for y in range(self.maxSizeY):
                if x == 0:
                    self.canvas.putPoint(x, y, "\033[0;0;47m ")
                elif x == maxSizeX-1:
                    self.canvas.putPoint(x, y, "\033[0;0;47m ")
                if y == 0:                   
                    self.canvas.putPoint(x, y, "\033[0;0;47m ")
                elif y == maxSizeY-1: 
                    self.canvas.putPoint(x, y, "\033[0;0;47m ")
                if x in range(1, maxSizeX-1) and y in range(1, maxSizeY-1): 
                    self.canvas.putPoint(x, y, "\033[0;0;42m ")
                if x in self.lineCoordinates: 
                    self.canvas.putPoint(x, y, "\033[0;0;47m ") 
    def putPoint(self, x, y, character):
        self.canvas.putPoint(x, y, character)
    def clearPoint(self, x, y)
        self.canvas.clearPoint(x, y)
    def update(self, tileArray):
        self.canvas.update(tileArray)
    def drawField(self):
        self.canvas.drawCanvas()
