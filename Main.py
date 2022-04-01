from TeamController import *
from StadiumController import *

def Initialize(dataFolder):
    teams = getTeams(dataFolder)
    print("Teams loaded")
    stadiums = getStadiums(dataFolder)
    print("Stadiums loaded")
    return [teams, stadiums]

def main():
    initData = Initialize("Data")
    stadiumDrawables = []
    for stadium in initData[1]:
        stadiumDrawables.append(generateCanvas(int(stadium.x), int(stadium.y), "\033[0;0;42m ", "\033[0;0;47m ", stadium.localColor, stadium.visitorColor))
    stadiumDrawables[1].drawCanvas()
main()
