def loadPositionsFromCSV(path):
    positions = []
    with open(path, "r") as f:
        lines = f.readlines()
        for l in lines:
            if l[0] == "#":
                continue
            else:
                pos = l.split(",")
                pos[len(pos)-1] = pos[len(pos)-1].strip("\n") 
                positions.append((pos))
    return positions
