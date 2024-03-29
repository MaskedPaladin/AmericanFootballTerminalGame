from Playbook import *
from Play import *
import os

def loadPlaybook(dataFolder):
    plays = []
    playbooks = []
    formations = []
    actions = []
    playbooksFiles = os.listdir(dataFolder+"/Teams/Playbook")

    opened = False
    playTag = None
    stereotype = None
    name = None

    for p in playbooksFiles:
        with open(dataFolder+"/Teams/Playbook/"+p, "r") as f:
            lines = f.readlines()
            for l in lines:
                l = l.strip("\n")
                if l[0] == "#":
                    continue
                if l[0] == "-":
                    fields = l.split(" ")
                    stereotype = fields[1]
                if l[0] == "@":
                    opened = True
                    plays = []
                    fields = l.split(" ")
                    playTag = l
                    name = fields[1]
                if l[0] == "*" and opened == True:
                    formation = (l[2:].split(","))
                    formations.append(formation)
                if l[0] == "+" and opened == True:
                    action = (l[2:].split(","))
                    actions.append(action)
                if l == playTag:
                    plays.append(Play(name, formations, actions))
                    formations = []
                    actions = []
        playbooks.append(Playbook(p, stereotype, plays))

        plays = []
        opened = False
        playTag = None
        stereotype = None
        name = None
    return playbooks
