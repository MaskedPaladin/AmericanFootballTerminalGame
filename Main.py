from Menu import *

from PlayerController import *
from TeamController import *
from FieldController import *



def Initialize(dataFolder):
    players = PlayerController.getPlayers(dataFolder)
    teams = TeamController.getTeams(dataFolder)
    fields = FieldController.getFields(dataFolder)
    return [players, teams, fields]

def main():
    initData = Initialize("Data")
    while True:
        mainMenu()
