from TeamController import *
from StadiumController import *

def Initialize(dataFolder):
    teams = getTeams(dataFolder)
    stadiums = getStadiums(dataFolder)
    return [teams, stadiums]

def main():
    initData = Initialize("Data")
    stadiumDrawables = []
    for stadium in initData[1]:
        stadiumDrawables.append(generateCanvas(int(initData[1][0].x), int(initData[1][0].y), "\033[0;0;42m ", "\033[0;0;47m ", "\033[0;0;41m ", "\033[0;0;44m "))
    stadiumDrawables[0].drawCanvas()

main()
