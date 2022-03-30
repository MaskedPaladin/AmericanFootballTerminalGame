import Player as P
import Team as T
import Canvas as C
import Field as F
import PlayerController as PC
import PlaybookController as PBC
import Match as M



playersA = PC.loadFromCSV("Data/TeamA/players.csv")
playbookA = PBC.loadFromCSV()
teamA = T.Team("TeamA")
match = M.Match()
