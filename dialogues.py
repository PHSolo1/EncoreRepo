class Dialogue:
    def __init__(name):
        paroles = []
        with open("demofile.txt", "r") as f:
            for line in f:
                splited = line.split(";")
                paroles.append({personnage: splited[0], paroles: splited[1]})
    def loadLine(index):
        return paroles[index]