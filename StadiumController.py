from Stadium import *
from Canvas import *

def generateCanvas(xSize, ySize, grassCharacter, lineCharacter, teamACharacter, teamBCharacter):
    canvas = Canvas(xSize,ySize)
    for x in range(xSize):
        for y in range(ySize):
            if x in range(int(xSize/10)):
                canvas.putPoint(x, y, teamACharacter)
            elif x in range(int(xSize-xSize/10), xSize):
                canvas.putPoint(x, y, teamBCharacter)
            if x == 0:
                canvas.putPoint(x, y, lineCharacter)
            elif x == xSize-1:
                canvas.putPoint(x, y, lineCharacter)
            elif y == 0:
                canvas.putPoint(x, y, lineCharacter)
            elif y == ySize-1:
                canvas.putPoint(x, y, lineCharacter)
            else:
                canvas.putPoint(x, y, grassCharacter)
            if y == int(ySize/4):
                canvas.putPoint(x, y, lineCharacter)
            elif y == int((ySize-ySize/4)-1):
                canvas.putPoint(x, y, lineCharacter)
            if x in range(1, int(xSize/10)) and y in range(1, ySize-1):
                canvas.putPoint(x, y, teamACharacter)
            if x == int(xSize/10-1):
                canvas.putPoint(x, y, lineCharacter)
            elif x in range(int(xSize-xSize/10), xSize-1) and y in range(1, ySize-1):
                canvas.putPoint(x, y, teamBCharacter)
            if x == int(xSize-xSize/10):
                canvas.putPoint(x, y, lineCharacter)
            if x in range(int((xSize/10)-1), int((xSize-xSize/10)-1), int((xSize/24))):
                canvas.putPoint(x, y, lineCharacter)
    return canvas


def getStadiums(dataFolder):
    stadiums = []
    with open(dataFolder+"/Stadiums/"+"fields.csv") as f:
        lines = f.readlines()
        for l in lines:
            if l[0] != "#":
                l = l.strip("\n")
                fields = l.split(",")
                stadiums.append(Stadium(fields[1],fields[2],"\033[0;0;"+fields[3]+"m ","\033[0;0;"+fields[4]+"m "))
            else:
                continue
    return stadiums
