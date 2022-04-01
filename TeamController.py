from Player import *
from Team import *
import os

def getTeams(dataFolder):
    name = None
    players = []
    teams = []
    opened = False
    closeTag = None

    for t in os.listdir(dataFolder+"/Teams/Players"):
        with open(dataFolder+"/Teams/Players/"+t, "r") as f:
            lines = f.readlines()
            for l in lines:
                if l[0] == "#" or l == None:
                    continue
                elif l[0] == "@" and opened is False:
                    opened = True
                    fields = l.split(" ")
                    name = fields[1]
                    closeTag = l
                elif opened is True and l[0] == "+":
                    fields = l.split(",")
                    players.append(Player(fields[0][2:], fields[1], fields[2], fields[3], fields[4], fields[5], fields[6], fields[7].strip("\n"))) 
                elif opened is True and l == closeTag:
                    teams.append(Team(name, players))
                    name = None
                    players = []
                    opened = False
                    closeTag = None
    return teams
