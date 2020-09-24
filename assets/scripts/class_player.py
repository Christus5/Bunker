# -*- coding: utf-8 -*-
import ffc
import random

class Player:
    def __init__(self, professions, sex, hobbies, lifeConditions, inventory, phobias, characters, additionalinfos):
        self.profession = ffc.chooseFromList(professions)
        self.sex = ffc.chooseFromListDR(sex)
        self.age = Player.getAge()
        self.hobby = ffc.chooseFromList(hobbies)
        self.lifeCondition = Player.chooseLifeCondition(lifeConditions)
        self.item = ffc.chooseFromList(inventory)
        self.phobia = ffc.chooseFromList(phobias)
        self.character = ffc.chooseFromList(characters)
        self.additionalInfo = ffc.chooseFromList(additionalinfos)
        
    def out(self, i):
        filename = "setup/players/player" + str(i) + ".txt"
        fileloc = open(filename, 'w')
        fileloc.write(self.info())
        fileloc.close()
        
    def info(self):
        return f"""Profession: {self.profession}
Sex: {self.sex}
Age: {self.age}
Hobby: {self.hobby}
Life condition: {self.lifeCondition}
Item in inventory: {self.item}
Phobia: {self.phobia}
Character: {self.character}
Additional information: {self.additionalInfo}"""

    #getting age (chance is lower from 46)
    @staticmethod
    def getAge():
        rand = random.random() + 0.39
        if rand > 1:
            rand = 1
        
            age = random.randint(18, 80)
            
            if age > 45:
                age = age * rand
                
            return int(age)

    
    #it'll choose from list but items should be repeated except the first
    @staticmethod
    def chooseLifeCondition(listName):
        rand = random.randint(0, len(listName) - 1)
        
        if rand == 0:
            return listName[0]
        
        returnValue = listName[rand]
        listName.remove(listName[rand])
        return returnValue