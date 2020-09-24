# -*- coding: utf-8 -*-
import sys
import os

sys.path.insert(1, "assets/scripts")
import class_player
import class_enviroment
import class_bunker

MAX_PLAYER_COUNT = 12

#main function
def main():
    print(f"\nMax player count: {MAX_PLAYER_COUNT}\n")
    players = initPlayers()
    handleExtraFiles(len(players))
    enviroment = initEnviroment()
    bunker = initBunker(len(players))
    output(players, enviroment, bunker)
    print("Game generation done")
    print(f"\nEnviroment: \n\t{enviroment.info()}")
    print(f"Bunker: \n\t{bunker.info()}")
    input("\nPress enter to exit")

"""GLOBAL FUNCTIONS"""
#read from file and append to list
def readFile(file):
    newList = []
    for item in file:
        newList.append(item.rstrip('\n'))
    
    return newList
#------------------------------------------------------------------------------
#checks user input and validates it(not to crash program)
def userInput():
    try:
        return int(input("Enter player count: "))
    except ValueError:
        return userInput()
#------------------------------------------------------------------------------
def output(players, enviroment, bunker):
    for i in range(len(players)):
        players[i].out(i + 1)
    enviroment.out()
    bunker.out()
#------------------------------------------------------------------------------
def handleExtraFiles(playerCount):
    for i in range(playerCount, MAX_PLAYER_COUNT):
        fileName = "setup/players/player" + str(i + 1) + ".txt"
        if os.path.exists(fileName):
            os.remove(fileName)
#------------------------------------------------------------------------------
#initialize players stats/info
def initPlayers():
    #read info from txt files
    cLoc = "assets/characters/"
    professions = open(cLoc + "professions.txt")
    hobbies = open(cLoc + "hobbies.txt")
    sex = open(cLoc + "sex.txt")
    lifeConditions = open(cLoc + "life_conditions.txt")
    inventory = open(cLoc + "inventory.txt")
    phobias = open(cLoc + "phobias.txt")
    characters = open(cLoc + "characters.txt")
    additionalInfo = open(cLoc + "additional_information.txt")
    
    #create a lists from file info
    profList = readFile(professions)
    sex = readFile(sex)
    hobbies = readFile(hobbies)
    lifeConditions = readFile(lifeConditions)
    inventory = readFile(inventory)
    phobias = readFile(phobias)
    characters = readFile(characters)
    additionalInfo = readFile(additionalInfo)
    
    #get player count from a user
    playerCount = userInput()
    
    #players list (class Player objects)
    players = []
        
    #fill players list
    for x in range(playerCount):
        tmp = class_player.Player(profList, sex, hobbies, lifeConditions, inventory, phobias, characters, additionalInfo)
        players.append(tmp)

    return players
#------------------------------------------------------------------------------
#initialize enviroment
def initEnviroment():
    #read info from txt files
    eLoc = "assets/enviroment/" 
    disasters = open(eLoc + "disasters.txt")
    
    #create list from file info
    disasters = readFile(disasters)
    
    #create Enviroment class object
    enviroment = class_enviroment.Enviroment(disasters)
    
    return enviroment
#------------------------------------------------------------------------------
#initialize bunker
def initBunker(playerCount):
    bunker = class_bunker.Bunker(playerCount)
    
    return bunker

    
    
main()