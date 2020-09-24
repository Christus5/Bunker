# -*- coding: utf-8 -*-
import ffc

class Bunker:
    def __init__(self, playerCount):
        self.maxSurvivors = int(playerCount / 2)
    def out(self):
        fileLoc = open("setup/bunker.txt", 'w')
        fileLoc.write(self.info())
        fileLoc.close()
    def info(self):
        return f"""Place for suriviors: {self.maxSurvivors}"""