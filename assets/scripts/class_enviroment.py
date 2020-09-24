# -*- coding: utf-8 -*-
import ffc

class Enviroment:
    def __init__(self, disaster):
        self.disaster = ffc.chooseFromListDR(disaster)
    def out(self):
        filename = "setup/enviroment.txt"
        fileloc = open(filename, 'w')
        fileloc.write(self.info())
        fileloc.close()
    def info(self):
        return f"""Disaster: {self.disaster}"""