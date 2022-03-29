import Player as p
def loadFromCSV():
    players = []
    with open ("players.csv", "r") as f:
        lines = f.readlines()[1:]
        for line in lines:
            l = line.split(",")
            players.append(p.Player(l[0], l[1], l[2], l[3], int(l[4]), int(l[5]), int(l[6]), int(l[7]), int(l[8]), int(l[9]), int(l[10]), int(l[11]), int(l[12]), int(l[13]), int(l[14]), int(l[15]), int(l[16]), int(l[17]), int(l[18]), int(l[19]), int(l[20]), int(l[21].strip("\n"))))
    return players
