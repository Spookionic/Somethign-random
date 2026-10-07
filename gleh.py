# imports
import random
import time

# Functions
def Random_Role_Event(role):
    Murder = ["Lights out", "Increased Vision", "Insanity", "Increased Movement speed"]
    Civilian = ["Decreased Movement Speed", "Decreased Vision", "Tiredness", "Weakness", "Hallucinations"]
    Sherif = ["placeholder"]

    if role == "Murder":
        Murder_Out = random.choice(Murder)
        return Murder_Out
    if role == "Civilian":
        Civilian_Out = random.choice(Civilian)
        return Civilian_Out
    if role == "Sherif":
        Sherif_Out = random.choice(Sherif)
        return Sherif_Out

def Role_Pick():
    roles = ["Murder"]
    otherrole = ["Civilian", "Sherif"]
    return random.choice(roles)

# BackEnd Stuff
MurderRole = False
SherifRole = False
CivilianRole = True

Role = Role_Pick()
if Role == "Murder":
    MurderRole = True
if Role == "Sherif":
    SherifRole = True
if Role == "Civilian":
    CivilianRole = True
# Murder Gameplay
if MurderRole:
    print("???: Welcome to the Hogwarts Train!")
    time.sleep(2)
    print("???: Inspired by the famous novel Harry Potter, this train is designed to emulate that experience!")
    time.sleep(3)
    print("Soyocho: My name is Soyocho, and I will be your tour for th-")
    time.sleep(3)
    print("\nThe lights go out...Soyocho is found dead.")