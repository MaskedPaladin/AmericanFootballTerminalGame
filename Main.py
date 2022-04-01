from TeamController import *
from StadiumController import *

def Initialize(dataFolder):
    teams = getTeams(dataFolder)
    print("Teams loaded")
    for t in teams:
        print("@",t.name)
        for p in t.players:
            print("+",p.name,p.surname1,p.surname2,p.position)
    stadiums = getStadiums(dataFolder)
    print("Stadiums loaded")
    return [teams, stadiums]

def main():
    initData = Initialize("Data")
    stadiumDrawables = []
    for stadium in initData[1]:
        stadiumDrawables.append(generateCanvas(int(stadium.x), int(stadium.y), "\033[0;0;42m ", "\033[0;0;47m ", stadium.localColor, stadium.visitorColor))
main()
