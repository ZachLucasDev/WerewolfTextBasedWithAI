class Player:
    playerName = ""
    dead = False
    win = False
    cultMember = False
    protected = False
    
    def __init__(self, obj):
        self.myClass = (obj)
        if(obj.className == "CultLeader"):
            cultMember = True
    
    def accuse(players):
        return int(input("Which player do you want to accuse?"))
    pass
    
    def createRoleList(self, targets):
        if(self.myClass.team == 2):
            for player in targets:
                temp = []
                temp.append(player.playerName)
                if(player.dead):
                    temp.append(player.myClass.className)
                else:
                    if(player.myClass.className == "Werewolf"):
                        #Werewolves know who other werewolves are
                        temp.append(player.myClass.className)
                    else:
                        temp.append("Unknown")
                temp.append(player.dead)
                temp.append(0) #suspect counter
                temp.append(player.myIndex)
                self.knownPlayerRoles.append(temp)
        else:
            for player in targets:
                temp = []
                temp.append(player.playerName)
                if(player.dead):
                    temp.append(player.myClass.className)
                else:
                    temp.append("Unknown")
                temp.append(player.dead)
                temp.append(0) #suspect counter
                temp.append(player.myIndex)
                self.knownPlayerRoles.append(temp)
    
    def updateDeadRoles(self, targets):
        for object in self.knownPlayerRoles:
            for player in targets:
                if(object[0] == player.playerName):
                    if(player.dead):
                        object[1] = player.myClass.className
                        object[2] = player.dead
    
    def updateSuspects(self, event):
        word_list = event.split()
        for player in self.knownPlayerRoles:
            if(player[0] == word_list[0]):
                if(self.myClass.className == "Tanner"):
                    if("claimed" in event): 
                        if(player[0] == "Unknown"):
                            player[1] = "claimed "+ word_list[-1]
                            if(word_list[-1] == "Seer"):
                                player[3] == 100
                            elif (word_list[-1] == "Hunter"):
                                player[3] == 0
                            elif (word_list[-1] == "BodyGuard"):
                                player[3] == 0
                            elif (word_list[-1] == "ApprenticeSeer"):
                                player[3] += 50
                                if(player[3] > 100):
                                    player[3] = 100
                            else:
                                player[3] += 10
                                if(player[3] > 100):
                                    player[3] = 100
                            if(player[1] == "Werewolf"):
                                player[3] == 100
                        else:
                            player[3] += 20
                            if(player[3] > 100):
                                player[3] = 100
                    elif("accuse" in event):
                        player[3] += 10
                        if(player[3] > 100):
                            player[3] = 100
                        for accused in self.knownPlayerRoles:
                            if(accused[0] == word_list[-1]):
                                accused[3] -= 10
                                if(accused[3] < 0):
                                    accused[3] = 0
                    elif("nothing" in event):
                        player[3] += 5
                        if(player[3] > 100):
                            player[3] = 100
                elif(self.myClass.className == "CultLeader"):
                    if("claimed" in event): 
                        if(player[0] == "Unknown"):
                            player[1] = "claimed "+ word_list[-1]
                            if(word_list[-1] == "Seer"):
                                player[3] == 0
                            elif (word_list[-1] == "Hunter"):
                                player[3] == 100
                            elif (word_list[-1] == "BodyGuard"):
                                player[3] == 0
                            elif (word_list[-1] == "ApprenticeSeer"):
                                player[3] == 0
                            else:
                                player[3] += 10
                                if(player[3] > 100):
                                    player[3] = 100
                            if(player[1] == "Werewolf"):
                                player[3] == 100
                        else:
                            player[3] += 20
                            if(player[3] > 100):
                                player[3] = 100
                    elif("accuse" in event):
                        #Trust seer
                        if(player[1] == "Seer"):
                            for accused in self.knownPlayerRoles:
                                if(accused[0] == word_list[-1]):
                                    accused[3] == 100
                        else:
                            player[3] += 10
                            if(player[3] > 100):
                                player[3] = 100
                            for accused in self.knownPlayerRoles:
                                if(accused[0] == word_list[-1]):
                                    accused[3] += 10
                                    if(accused[3] > 100):
                                        accused[3] = 100
                    elif("nothing" in event):
                        player[3] += 5
                        if(player[3] > 100):
                            player[3] = 100
                elif(self.myClass.team == 2):
                    if("claimed" in event): 
                        if(player[0] == "Unknown"):
                            player[1] = "claimed "+ word_list[-1]
                            if(word_list[-1] == "Seer"):
                                player[3] == 100
                            elif (word_list[-1] == "Hunter"):
                                player[3] == 0
                            elif (word_list[-1] == "BodyGuard"):
                                player[3] == 100
                            elif (word_list[-1] == "ApprenticeSeer"):
                                player[3] == 100
                            else:
                                player[3] += 10
                                if(player[3] > 100):
                                    player[3] = 100
                        else:
                            player[3] += 20
                            if(player[3] > 100):
                                player[3] = 100
                        if(player[1] == "Werewolf"):
                            player[3] == 0
                        else:
                            player[3] += 10
                            if(player[3] > 100):
                                player[3] = 100
                    elif("accuse" in event):
                        player[3] += 10
                        if(player[3] > 100):
                            player[3] = 100
                        for accused in self.knownPlayerRoles:
                            if(accused[0] == word_list[-1]):
                                if(accused != "Werewolf"):
                                    accused[3] += 10
                                    if(accused[3] < 0):
                                        accused[3] = 0
                    elif("nothing" in event):
                        if(player[1] != "Werewolf"):
                            player[3] += 5
                            if(player[3] > 100):
                                player[3] = 100
                else:
                    #Handle town
                    if("claimed" in event): 
                        if(player[0] == "Unknown"):
                            player[1] = "claimed "+ word_list[-1]
                            if(word_list[-1] == "Seer"):
                                player[3] -= 65
                                if(player[3] < 0):
                                    player[3] = 0
                            elif (word_list[-1] == "Hunter"):
                                player[3] -= 20
                                if(player[3] < 0):
                                    player[3] = 0
                            elif (word_list[-1] == "BodyGuard"):
                                player[3] -= 50
                                if(player[3] < 0):
                                    player[3] = 0
                            elif (word_list[-1] == "ApprenticeSeer"):
                                player[3] -= 30
                                if(player[3] < 0):
                                    player[3] = 0
                            else:
                                player[3] += 10
                                if(player[3] > 100):
                                    player[3] = 100
                            if(player[1] == "Werewolf"):
                                player[3] == 100
                            else:
                                player[3] += 10
                                if(player[3] > 100):
                                    player[3] = 100
                        else:
                            player[3] += 20
                            if(player[3] > 100):
                                player[3] = 100
                        for deadPlayer in self.knownPlayerRoles:
                            if(deadPlayer[2] == True):
                                if(deadPlayer[1] == "Seer"):
                                    if(word_list[-1] == "Seer"):
                                        player[3] = 100
                                elif (deadPlayer[1] == "BodyGuard"):
                                    if(word_list[-1] == "BodyGuard"):
                                        player[3] = 100
                                elif (deadPlayer[1] == "ApprenticeSeer"):
                                    if(word_list[-1] == "ApprenticeSeer"):
                                        player[3] = 100
                        
                    elif("accuse" in event):
                        #Trust seer
                        if(player[1] == "Seer"):
                            for accused in self.knownPlayerRoles:
                                if(accused[0] == word_list[-1]):
                                    accused[3] == 100
                        else:
                            player[3] += 10
                            if(player[3] > 100):
                                player[3] = 100
                            for accused in self.knownPlayerRoles:
                                if(accused[0] == word_list[-1]):
                                    accused[3] += 20
                                    if(accused[3] > 100):
                                        accused[3] = 100
                    elif("nothing" in event):
                        player[3] += 5
                        if(player[3] > 100):
                            player[3] = 100
##
class Tanner(Player):
    className = "Tanner"
    team = 0
    NightAbility = False
    DeathAbility = False
            
class Werewolf(Player):
    className = "Werewolf"
    team = 2
    NightAbility = True
    DeathAbility = False
        
    def nightAbility(targets, bot):
        
        while(True):
            choice = bot.getKillTarget(targets)
            if(targets[choice].myClass.team != 2):
                break
        return choice

class Seer(Player):
    className = "Seer"
    team = 1
    NightAbility = True
    DeathAbility = True
    
    def nightAbility(targets, bot):
        bot.getSeerTarget(targets)
        return ("Null")
    
    def deathAbility(targets):
        #find app Seer and activate their night ability
        for player in targets:
            if(player.myClass.className == "ApprenticeSeer" ):
                player.myClass.NightAbility = True
        NightAbility = True

class Villager(Player):
    className = "Villager"
    team = 1
    NightAbility = False
    DeathAbility = False

class BodyGuard(Player):
    className = "BodyGuard"
    team = 1
    NightAbility = True
    DeathAbility = False

    def nightAbility(targets, bot):
        index = bot.getSaveTarget(targets)
        targets[index].protected = True
        return ("Bodyguard guarded "+targets[index].playerName)
        
class Hunter(Player):
    className = "Hunter"
    team = 1
    NightAbility = False
    DeathAbility = True

    def deathAbility(targets, bot):
        return bot.getKillTarget(targets)
            
class ApprenticeSeer(Player):
    className = "ApprenticeSeer"
    team = 1
    NightAbility = False
    DeathAbility = False
        
    def nightAbility(targets, bot):
        bot.getSeerTarget(targets)
        return ("Null")
         
class CultLeader(Player):
    className = "CultLeader"
    team = 0
    NightAbility = True
    DeathAbility = False

    def nightAbility(targets, bot):
        index = bot.getCLTarget(targets)
        targets[index].cultMember = True
        total = 0
        for player in targets:
            if(player.cultMember):
                total += 1
        
        return ("Cult leader has covered " + str(total) + " town members")
##

        
class HumanPlayer(Player):
    suspitions = [0,0,0,0,0,0,0,0,0]
    knownPlayerRoles = []
    roleCalled = False
    clamedRole = ""
    
    def __init__(self, obj, index):
        self.clamedRole = ""
        self.roleCalled = False
        self.knownPlayerRoles = []
        super().__init__(obj)
        self.myIndex = index
    
    def updateIndex(self, newIndex):
        self.myIndex = newIndex
           
    def actionOne(self):
        return int(input(self.playerName + ", What would you like to do? \n1. Say Nothing \n2. Claim role \n3. Accuse a player"))
        
    def sayRole(self, claimed):
        if(claimed == False):
            roleCalled = True
            clamedRole = input(super().playerName + ", what role do you claim?")
        return clamedRole
        
    def accusePlayer(self, targets):
        return int(input(super().playerName + ", Who do you accuse (-1 for no one or number from 0 - 9"))
            
    def getCLTarget(self,targets):
        self.cultMember = True
        return int(input("Add player to cult"))
    
    def getSeerTarget(self, targets):
        choice = int(input("Who do you look at seer?"))
        if(targets[choice].myClass.team == 2):
            return ("Werewolf")
        
        return ("Not werewolf")
    
    def getKillTarget(self, targets):
        return int(input("Whould do you want to kill"))
        
    def getSaveTarget(self, targets):
        return int(input("Whould do you want to save"))
        
    def vote(self, target):
        return int(input("1 to kill, -1 to save, 0 to abstain"))    
##
class RandomBot(Player):
    import random
    
    def __init__(self, obj, index):
        self.botType = "RandomBot"
        self.clamedRole = ""
        self.roleCalled = False
        self.knownPlayerRoles = []
        super().__init__(obj)
        self.myIndex = index
    
    def updateIndex(self, newIndex):
        self.myIndex = newIndex
           
    def actionOne(self):
        return random.randint(1,4)
        
    def sayRole(self,claimed):
        # Will not claim evil roles 
        if(claimed == False):
            roleCalled = True
            choice = random.randint(1,4)
            if(choice == 1):
                clamedRole = "Seer"
            elif (choice == 2):
                clamedRole = "Hunter"
            elif (choice == 3):
                clamedRole = "Villager"
            elif (choice == 4):
                clamedRole = "BodyGuard"
            elif (choice == 5):
                clamedRole = "ApprenticeSeer"
        return clamedRole
        
    def accusePlayer(self, targets):
        #print("Stuck in accusePlayer")
        for player in self.knownPlayerRoles:
            if("Werewolf" in player[1]):
                for i, x in enumerate(targets):
                    if player[0] == x.playerName:
                        if(x.playerName != self.playerName):
                            return i
        while(True):
            choice = random.randint(-1,len(targets)-1)
            if(choice < 0):
                break
            elif(targets[choice].playerName != super().playerName):
                break
        return choice
            
    def getCLTarget(self, targets):
        #print("Stuck in getCLTarget")
        self.cultMember == True
        while(True):
            choice = random.randint(0,len(targets)-1)
            if(targets[choice].playerName != super().playerName):
                if(targets[choice].cultMember == False):
                    break
        return choice
    
    def getSeerTarget(self, targets):
        #print("Stuck in seerTarget")
        #Give it 20 trys before returning no target
        counter = 0
        while(counter < 20):
            choice = random.randint(0,len(self.knownPlayerRoles)-1)
            if(self.knownPlayerRoles[choice][0] != super().playerName):
                if(self.knownPlayerRoles[choice][1] == "Unknown"):
                    index = 0
                    for player in targets:
                        if(player.playerName == self.knownPlayerRoles[choice][0]):
                            break
                        index += 1
                    if(targets[index].myClass.team == 2):
                        self.knownPlayerRoles[choice][1] = "Werewolf"
                    return choice
            counter += 1
        return -1
    
    def getKillTarget(self, targets):
        #print("Stuck in Kill target")
        while(True):
            choice = random.randint(0,len(targets)-1)
            if(targets[choice].playerName != super().playerName):
                break
        return choice
        
    def getSaveTarget(self, targets):
        #print("Stuck in savetarget")
        choice = random.randint(0,len(targets)-1)
        return choice
        
    def vote(self, target):
        return random.randint(-1,2) 
##
class AggressiveBot (Player):
    import random
    
    def __init__(self, obj, index):
        self.botType = "AggressiveBot"
        self.clamedRole = ""
        self.roleCalled = False
        self.knownPlayerRoles = []
        super().__init__(obj)
        self.myIndex = index
    
    def updateIndex(self, newIndex):
        self.myIndex = newIndex
         
    def actionOne(self):
        #Always accuse someone. So return 3
        return 3
        
    def sayRole(self,claimed):
        if(claimed == False):
            roleCalled = True
            if(self.myClass.team == 1):
                #If town, dont lie
                clamedRole = self.myClass.className
            else:
                # Will not claim evil roles 
                choice = random.randint(1,4)
                if(choice == 1):
                    clamedRole = "Seer"
                elif (choice == 2):
                    clamedRole = "Hunter"
                elif (choice == 3):
                    clamedRole = "Villager"
                elif (choice == 4):
                    clamedRole = "BodyGuard"
                elif (choice == 5):
                    clamedRole = "ApprenticeSeer"
        return clamedRole
        
    def accusePlayer(self, targets):
        #print("Stuck in accuse targets")
        #loops until the first player with the highest suspect count is found. if no one is a suspect, randomly accuse.
        counter = 100
        notFound = True
        while(notFound):
            if(counter > 20):
                for player in self.knownPlayerRoles:
                    if("Werewolf" in player[1]):
                        for i, x in enumerate(targets):
                            if player[0] == x.playerName:
                                if(x.playerName != self.playerName):
                                    choice = i
                                    notFound = False
                    elif(player[3] == counter):
                        for i, x in enumerate(targets):
                            if player[0] == x.playerName:
                                if(x.playerName != self.playerName):
                                    choice = i
                                    notFound = False
                                    break
            else:
                choice = random.randint(0,len(targets)-1)
                if(targets[choice].playerName != self.playerName):
                    notFound = False
            counter -= 5
        return choice
            
    def getCLTarget(self, targets):
        #print("I %s am the cult leader" % self.playerName)
        self.cultMember = True
        #print("Stuck in cult leader targets")
        #Target the player with the lowest suspect rating that is not already a cult member
        notFound = True
        while(notFound):
            choice = random.randint(0,len(targets)-1)
            if(targets[choice].playerName != self.playerName):
                if(targets[choice].cultMember == False):
                    notFound = False
        return choice
    
    def getSeerTarget(self, targets):
        #print("Stuck in seer targets")
        randomGuesses = 20 #This ensures that you will at least attempt to pick someone other then yourself
        while(randomGuesses > 0):
            choice = random.randint(0,len(self.knownPlayerRoles)-1)
            if(self.knownPlayerRoles[choice][0] != self.playerName):
                if(self.knownPlayerRoles[choice][1] == "Unknown"):
                    index = 0
                    for i, player in enumerate(targets):
                        if(player.playerName == self.knownPlayerRoles[choice][0]):
                            index = i
                            break
                    if(targets[index].myClass.team == 2):
                        self.knownPlayerRoles[choice][1] = "Werewolf"
                    return choice
            randomGuesses -= 1
        #If all players are not a suspect and the computer either knows everyones role or somehow chose himself 20 times
        return -1
    
    def getKillTarget(self, targets):
        #print("Stuck in kill targets")
        notFound = True
        while(notFound):
            choice = random.randint(0,len(targets)-1)
            if(targets[choice].playerName != self.playerName):
                notFound = False
        return choice
        
    def getSaveTarget(self, targets):
        #print("Stuck in save targets")
        #Target the player with the lowest suspect rating that is not already a cult member
        notFound = True
        while(notFound):
            choice = random.randint(0,len(targets)-1)
            if(targets[choice].playerName != self.playerName):
                notFound = False
        return choice
        
    def vote(self, target):
        counter = 0
        while(True):
            if(counter < 20):
                for i, player in enumerate(self.knownPlayerRoles):
                    if(player[3] == counter):
                        if(target.playerName == player[0]):
                            choice = -1
                            break
            else:
                choice = 1
                break
            counter += 5
        return choice
        
##
class PassiveBot (Player):
    import random
    
    def __init__(self, obj, index):
        self.botType = "PassiveBot"
        self.clamedRole = ""
        self.roleCalled = False
        self.knownPlayerRoles = []
        super().__init__(obj)
        self.myIndex = index
        
    
    def updateIndex(self, newIndex):
        self.myIndex = newIndex
        
    def actionOne(self):
        #Always do nothing. So return 1
        return 1
        
    def sayRole(self,claimed):
        if(claimed == False):
            roleCalled = True
            if(self.myClass.team == 1):
                #If town, dont lie
                clamedRole = self.myClass.className
            else:
                # Will not claim evil roles 
                choice = random.randint(1,4)
                if(choice == 1):
                    clamedRole = "Seer"
                elif (choice == 2):
                    clamedRole = "Hunter"
                elif (choice == 3):
                    clamedRole = "Villager"
                elif (choice == 4):
                    clamedRole = "BodyGuard"
                elif (choice == 5):
                    clamedRole = "ApprenticeSeer"
        return clamedRole
        
    def accusePlayer(self, targets):
        #Will accuse a player only if they are almost 100% a suspect
        counter = 100
        notFound = True
        while(notFound):
            if(counter == 100):
                for player in self.knownPlayerRoles:
                    if("Werewolf" in player[1]):
                        for i, x in enumerate(targets):
                            if player[0] == x.playerName:
                                if(x.playerName != self.playerName):
                                    choice = i
                                    notFound = False
                    elif(player[3] == counter):
                        for i, x in enumerate(targets):
                            if player[0] == x.playerName:
                                if(x.playerName != self.playerName):
                                    choice = i
                                    notFound = False
            else:
                choice = -1
                notFound = False
            counter -= 5
        return choice
            
    def getCLTarget(self, targets):
        self.cultMember = True
        #Target the player with the lowest suspect rating that is not already a cult member
        notFound = True
        while(notFound):
            choice = random.randint(0,len(targets)-1)
            if(targets[choice].playerName != self.playerName):
                if(targets[choice].cultMember == False):
                    notFound = False
        return choice
    
    def getSeerTarget(self, targets):
        randomGuesses = 20 #This ensures that you will at least attempt to pick someone other then yourself
        while(randomGuesses > 0):
            choice = random.randint(0,len(self.knownPlayerRoles)-1)
            if(self.knownPlayerRoles[choice][0] != self.playerName):
                if(self.knownPlayerRoles[choice][1] == "Unknown"):
                    index = 0
                    for i, x in enumerate(targets):
                        if(x.playerName == self.knownPlayerRoles[choice][0]):
                            break
                        index = i
                    if(targets[index].myClass.team == 2):
                        self.knownPlayerRoles[choice][1] = "Werewolf"
                    return choice
            randomGuesses -= 1
        #If all players are not a suspect and the computer either knows everyones role or somehow chose himself 20 times
        return -1
    
    def getKillTarget(self, targets):
        notFound = True
        while(notFound):
            choice = random.randint(0,len(targets)-1)
            #print("Randomly getting kill target")
            if(targets[choice].playerName != self.playerName):
                notFound = False
        return choice
        
    def getSaveTarget(self, targets):
        notFound = True
        while(notFound):
            choice = random.randint(0,len(targets)-1)
            if(targets[choice].playerName != self.playerName):
                notFound = False
        return choice
        
    def vote(self, target):
        counter = 100
        while(True):
            if(counter < 80):
                for i, player in enumerate(self.knownPlayerRoles):
                    if(player[3] == counter):
                        if(target.playerName == player[0]):
                            choice = 1
                            break
            else:
                choice = -1
                break
            counter -= 5
        return choice
        
##
class ProfMoriartyBot (Player):
    #This bot must play as the first player to function as intened. still working on making it function properly for other posistions
    import random
    import numpy as np
    
    def __init__(self, obj, index):
        self.botType = "ProfMoriartyBot"
        self.clamedRole = ""
        self.roleCalled = False
        self.knownPlayerRoles = []
        self.mySuspicionMeter = 0
        super().__init__(obj)
        self.myIndex = index
    
    def updateIndex(self, newIndex):
        self.myIndex = newIndex
        
    def median(self, lst):
        n = len(lst)
        if n < 1:
            return None
        if n % 2 == 1:
            return sorted(lst)[n//2]
        else:
            return sum(sorted(lst)[n//2-1:n//2+1])/2.0
            
    def updateMySuspicion(self):
        self.mySuspicionMeter += 10
        if(self.mySuspicionMeter > 100):
            self.mySuspicionMeter = 100
            
    def trackRoleCounts(self):
        seerCounter = 0
        BGCoutner = 0
        APCounter = 0
        HunterCOunter = 0
        villigercounter = 0
        for player in self.knownPlayerRoles:
            if(player[1] == "Seer"):
                seerCounter += 1
            elif (player[1]  == "Hunter"):
                HunterCOunter += 1
            elif (player[1]  == "BodyGuard"):
                BGCoutner += 1
            elif (player[1]  == "ApprenticeSeer"):
                APCounter += 1
            elif(player[1]  == "Villager"):
                villigercounter += 1
                
        for player in self.knownPlayerRoles:
            if(player[1] == "Seer"):
                if(seerCounter > 1):
                    player[3] == 100
                else:
                    player[3] == 0
            elif(player[1] == "BodyGuard"):
                if(BGCoutner > 1):
                    player[3] == 100
                else:
                    player[3] == 0
            elif(player[1] == "ApprenticeSeer"):
                if(APCounter > 1):
                    player[3] == 100
                else:
                    player[3] == 0
            elif(player[1] == "Hunter"):
                if(HunterCOunter > 3):
                    player[3] == 100
        
    def calculateOutcomesMeter(self, player):
        #Our Game thery calculation against a specific player
        choices = [(self.mySuspicionMeter + 5,player[3]),(self.mySuspicionMeter + 5,player[3] ),(self.mySuspicionMeter + 15,player[3]),
                    (self.mySuspicionMeter + 10,player[3] + 5),(self.mySuspicionMeter + 10,player[3] + 10),(self.mySuspicionMeter + 20,player[3] + 10),
                    (self.mySuspicionMeter + 10,player[3] + 15),(self.mySuspicionMeter + 10,player[3] + 20),(self.mySuspicionMeter + 20,player[3] + 20)]
        action1, action2, action3 = ([] for i in range(3))
        for i, obj in enumerate(choices):
            if(obj[0]<obj[1]):
                if(i < 3):
                    action1.append(1)
                elif(i <6):
                    action2.append(1)
                else:
                    action3.append(1)
            else:
                if(i < 3):
                    action1.append(0)
                elif(i <6):
                    action2.append(0)
                else:
                    action3.append(0)
        actions = [sum(action1[0:len(action1)]), sum(action2[0:len(action2)]), sum(action3[0:len(action3)])]
        actionSum = sum(actions)
        #Returns ([all indexs for highest rated actions], sum values of all actions, the player)
        return ([i for i, value in enumerate(actions) if value == max(actions)], actionSum, player)
        
    def actionOne(self):
        #Daily discution action
        choice = 1
        if(self.myClass.className == "Tanner"):
            #print(self.mySuspicionMeter)
            return 3
        elif(self.myClass.className == "CultLeader"):
            return 1
        else:
            possibleOutcomes = []
            numberOfAlivePlayers = 0
            for player in self.knownPlayerRoles:
                if( player[2] == False):
                    numberOfAlivePlayers += 1
                    possibleOutcomes.append(self.calculateOutcomesMeter(player))
            max = numberOfAlivePlayers * 9
            numberOfPosativeOutcomes = 0
            for outcome in possibleOutcomes:
                numberOfPosativeOutcomes += outcome[1]
            #On day 1 the numberOfPosativeOutcomes will be 48 so Threshold must be equal this or day 1 must be excludded from the option of revealing his role otherwise he will always choose reveal his role on day one.
            thresholdLower = max / 3 - (numberOfAlivePlayers - 2)#48 #To determin when things are too risky
            thresholdHigher = thresholdLower#96 #To determin when things are less risky
            if(numberOfPosativeOutcomes < thresholdLower):
                choice = 2 #Makes this choice when there is too many negative outcomes
            elif(numberOfPosativeOutcomes > thresholdHigher):
                choice = 3 #Makes this move when there is very lower negative outcomes
            else:
                choice = 1 #Makes this choice when there is a moderate amount of negative outcomes
                self.mySuspicionMeter += 5
            if(self.mySuspicionMeter > 100):
                self.mySuspicionMeter = 100
        return choice
        
    def sayRole(self,claimed): #May need to be changed
        #print("Stuck in sayRole")
        #When claiming a role, differnt things will have a differnet outcome. We will be cliaming one of the strategic roles that are availabe to be claimed. Hutner, Seer, Apprentice Seer, Body Guard, 
        if(claimed == False):
            self.roleCalled = True
            if(self.myClass.team == 1): #Be truthfull in your claim, no need to lie when you are a town member
                self.claimedRole = self.myClass.className 
            else: #Lie your ass off
                if(self.myClass.className == "Tanner"):
                    for deadPlayer in self.knownPlayerRoles:
                        if(deadPlayer[2] == True):
                            if(deadPlayer[1] == "Seer"):
                                self.claimedRole = "Seer"
                                break;
                            elif (deadPlayer[1] == "BodyGuard"):
                                self.claimedRole = "BodyGuard"
                                break;
                            elif (deadPlayer[1] == "ApprenticeSeer"):
                                self.claimedRole = "ApprenticeSeer"
                                break;
                        else:
                            self.claimedRole = "Werewolf"
                            
                elif(self.myClass.className == "CultLeader"):                
                        #these classes needs to keep both town and WW off them so they will claim Hunter as its class.
                        self.claimedRole = "Hunter"
                else:
                    if(self.mySuspicionMeter > 80): #Take a big risk becuase im screwed either way
                        self.claimedRole = "Seer"
                    elif(self.mySuspicionMeter > 50): #Take a mild risk and hope the heat is taken away
                        self.claimedRole = "BodyGuard"
                    else: #No need to be too risky
                        self.claimedRole = "ApprenticeSeer" 
            if(self.claimedRole == "Seer"):
                self.mySuspicionMeter -= 65
                if(self.mySuspicionMeter < 0):
                    self.mySuspicionMeter = 0
            elif(self.claimedRole == "BodyGuard"):
                self.mySuspicionMeter -= 50
                if(self.mySuspicionMeter < 0):
                    self.mySuspicionMeter = 0
            elif(self.claimedRole == "Hunter"):
                self.mySuspicionMeter -= 20
                if(self.mySuspicionMeter < 0):
                    self.mySuspicionMeter = 0
            elif(self.claimedRole == "ApprenticSeer"):
                self.mySuspicionMeter -= 30
                if(self.mySuspicionMeter < 0):
                    self.mySuspicionMeter = 0
            elif(self.claimedRole == "Werewolf"):
                self.mySuspicionMeter = 100
            else:
                self.mySuspicionMeter += 5
                if(self.mySuspicionMeter > 100):
                    self.mySuspicionMeter = 100
        return self.claimedRole
        
    def accusePlayer(self, targets):
        #print("Stuck in accuseplayer")
        if(self.myClass.className == "Tanner"):
            choice = -1
        if(self.myClass.className == "CultLeader"):
            #Accuse the most suspisious person
            choice = -1
            possibleOutcomes = []
            for player in self.knownPlayerRoles:
                if( player[2] == False):
                    possibleOutcomes.append(self.calculateOutcomesMeter(player))
            value = []
            for outcome in possibleOutcomes:
                value.append(outcome[1])
            index = min(enumerate(value), key=lambda x: abs(x[1]-100)) #Index of best target
            target = possibleOutcomes[index[0]][2]
            for i,player in enumerate(targets):
                if(player.playerName == target[0]): #Found target in list
                    choice = i
        else:
            #Get target best Target for my acusation best on median value
            choice = -1
            possibleOutcomes = []
            for player in self.knownPlayerRoles:
                if( player[2] == False):
                    possibleOutcomes.append(self.calculateOutcomesMeter(player))
            value = []
            for outcome in possibleOutcomes:
                value.append(outcome[1])
            med = self.median(value) 
            index = min(enumerate(value), key=lambda x: abs(x[1]-100)) #Index of best target
            target = possibleOutcomes[index[0]][2]
            for i,player in enumerate(targets):
                if(player.playerName == target[0]): #Found target in list
                    choice = i
        self.mySuspicionMeter += 10 #Update my suspision
        if(self.mySuspicionMeter > 100):
            self.mySuspicionMeter = 100
        return choice
            
    def getCLTarget(self, targets):
        self.cultMember = True
        #Target the player with the lowest suspect rating that is not already a cult member
        counter = 0
        notFound = True
        while(notFound):
            if(counter < 100):
                for player in self.knownPlayerRoles:
                    if(player[3] == counter):
                        for i, x in enumerate(targets):
                            if player[0] == x.playerName:
                                if(x.playerName != self.playerName):
                                    if(x.cultMember == False):
                                        choice = i
                                        notFound = False
            else:
                choice = random.randint(0,len(targets)-1)
                #print(targets[choice].playerName + ", "+ str(targets[choice].cultMember)+", "+ targets[choice].myClass.className)
                if(targets[choice].playerName != self.playerName):
                    if(targets[choice].cultMember == False):
                        notFound = False
            counter += 5
        return choice
    
    def getSeerTarget(self, targets):
        #print("Stuck in seertarget")
        #My Seer target will look at the second most suspicious person
        choice = -1
        possibleOutcomes = []
        for player in self.knownPlayerRoles:
            if( player[2] == False):
                possibleOutcomes.append(self.calculateOutcomesMeter(player))
        value = []
        for outcome in possibleOutcomes:
            if(outcome[2][1] == "Unknown"):
                value.append(outcome[1])
        if len(value) > 0:
            highest = min(enumerate(value), key=lambda x: abs(x[1]-80)) #Index of highest target
            del value[highest[0]]
            index = min(enumerate(value), key=lambda x: abs(x[1]-highest[0])) #Index of best target
            target = possibleOutcomes[index[0]][2]
            for i,player in enumerate(targets):
                if(player.playerName == target[0]): #Found target in list
                    choice = i
        return choice
    
    def getKillTarget(self, targets):
        #print("Stuck in kill targets")
        counter = 100
        notFound = True
        while(notFound):
            if(counter > 0):
                for player in self.knownPlayerRoles:
                    if(player[3] == counter):
                        for i, x in enumerate(targets):
                            if player[0] == x.playerName:
                                if(x.playerName != self.playerName):
                                    if(self.myClass.team == 2):
                                        if(x.myClass.team != 2):
                                            choice = i
                                            notFound = False
                                            break
                                    else:
                                        choice = i
                                        notFound = False
                                        break
            else:
                choice = random.randint(0,len(targets)-1)
                if(targets[choice].playerName != self.playerName):
                    notFound = False
            counter -= 5
        return choice
        
    def getSaveTarget(self, targets):
        #print("Stuck in savetarget")
        #Save the least suspicous person
        choice = -1
        possibleOutcomes = []
        for player in self.knownPlayerRoles:
            if( player[2] == False):
                possibleOutcomes.append(self.calculateOutcomesMeter(player))
        value = []
        for outcome in possibleOutcomes:
            value.append(outcome[1])
        if len(value) > 0:
            index = min(enumerate(value), key=lambda x: abs(x[1]-0)) #Index of best target
            target = possibleOutcomes[index[0]][2]
            for i,player in enumerate(targets):
                if(player.playerName == target[0]): #Found target in list
                    choice = i
        return choice
        
    def vote(self, target):
        #print("Stuck in vote")
        if(self.myClass.className == "Tanner"):
            return 1
        for player in self.knownPlayerRoles:
            if(player[0] == target.playerName):
                if(player[3] > 40):
                    return -1
        return 1
##
import random
from statistics import mode
townWins = 0
werewolfWins = 0
tannerWins = 0
cultLeaderWins = 0
myBotAsCL = 0
myBotAsWW = 0
myBotAsT = 0
myBotAsTown = 0
myBotWinCount = 0
RandomBotWinCounter = 0
AggressiveBotWinCounter = 0
PassiveBotWinCounter = 0
Draw = 0

def numberOfWins(players, winningTeam):
    global myBotWinCount
    global RandomBotWinCounter
    global AggressiveBotWinCounter
    global PassiveBotWinCounter
    global myBotAsCL
    global myBotAsWW 
    global myBotAsT 
    global myBotAsTown 
    for player in players:
        if(player.botType == "ProfMoriartyBot"):
            if(player.myClass.team == 1):
                if(winningTeam == "Villagers"):
                    myBotWinCount += 1
                    myBotAsTown += 1
            elif(player.myClass.team == 2):
                if(winningTeam == "Werewolves"):
                    myBotWinCount += 1
                    myBotAsWW += 1
            elif(player.myClass.className == "CultLeader"):
                if(winningTeam == "CultLeader"):
                    myBotAsCL += 1
                    myBotWinCount += 1
            else:
                if(winningTeam == "Tanner"):
                    myBotAsT += 1
                    myBotWinCount += 1
        elif(player.botType == "RandomBot"):
            if(player.myClass.team == 1):
                if(winningTeam == "Villagers"):
                    RandomBotWinCounter += 1
            elif(player.myClass.team == 2):
                if(winningTeam == "Werewolves"):
                    RandomBotWinCounter += 1
            elif(player.myClass.className == "CultLeader"):
                if(winningTeam == "CultLeader"):
                    RandomBotWinCounter += 1
            else:
                if(winningTeam == "Tanner"):
                    RandomBotWinCounter += 1
            
        elif(player.botType == "AggressiveBot"):
            if(player.myClass.team == 1):
                if(winningTeam == "Villagers"):
                    AggressiveBotWinCounter += 1
            elif(player.myClass.team == 2):
                if(winningTeam == "Werewolves"):
                    AggressiveBotWinCounter += 1
            elif(player.myClass.className == "CultLeader"):
                if(winningTeam == "CultLeader"):
                    AggressiveBotWinCounter += 1
            else:
                if(winningTeam == "Tanner"):
                    AggressiveBotWinCounter += 1
            
        elif(player.botType == "PassiveBot"):
            if(player.myClass.team == 1):
                if(winningTeam == "Villagers"):
                    PassiveBotWinCounter += 1
            elif(player.myClass.team == 2):
                if(winningTeam == "Werewolves"):
                    PassiveBotWinCounter += 1
            elif(player.myClass.className == "CultLeader"):
                if(winningTeam == "CultLeader"):
                    PassiveBotWinCounter += 1
            else:
                if(winningTeam == "Tanner"):
                    PassiveBotWinCounter += 1
                    
#Implement a check win function
def checkWin(players):
    wolfCount = 0
    neutralCount = 0
    villageCount = 0
    werewolfWin = False
    cultCounter = 0
    aliveCounter = 0
    cultLeaderAlive = False
    tannerAlive = False
    global cultLeaderWins
    global townWins
    global werewolfWins
    global tannerWins
    global Draw
    for player in players:
        if(player.dead == False):
            if(player.myClass.className == "CultLeader"):
                cultLeaderAlive = True
            if(player.myClass.className == "Tanner"):
                tannerAlive = True
            aliveCounter += 1
            if(player.myClass.team == 2):
                wolfCount += 1
            elif(player.myClass.team == 0):
                neutralCount += 1
            else:
                villageCount += 1
            if(player.cultMember):
                cultCounter += 1
    #Check if town wins
    if(wolfCount == 0 and cultLeaderAlive == False):
        #print("Town Wins!")
        townWins += 1
        numberOfWins(players, "Villagers")
        return True
    #Check if cultLeader wins
    if(cultCounter == aliveCounter):
        if(cultLeaderAlive):
            #print("CultLeader Wins!")
            cultLeaderWins += 1
            numberOfWins(players, "CultLeader")
            return True
    #Check Werewolves win
    if(wolfCount >= round(aliveCounter/2)):
        #print("Werewolves Wins!")
        werewolfWins += 1
        numberOfWins(players, "Werewolves")
        return True
    
    if(villageCount == 0 and wolfCount == 0):
        if(tannerAlive and cultLeaderAlive == False):
            #print("Tanner wins")
            tannerWins += 1
            numberOfWins(players, "Tanner")
            return True
        if(tannerAlive == False and cultLeaderAlive):
            #print("CultLeader wins")
            cultLeaderWins += 1
            numberOfWins(players, "CultLeader")
            return True
    
    if(villageCount == 0 and wolfCount == 0 and neutralCount == 0):
        #print("Everyone loses")
        Draw += 1
        return True
        
    return False
numberOfGames = 1000
counter = 0
while(counter < numberOfGames):
    print(counter)
    Cards = [ Tanner, Werewolf, Werewolf, Werewolf, BodyGuard, Seer, Hunter, ApprenticeSeer, CultLeader, Villager, Villager, Villager, Villager, Villager, Villager, Villager]
    random.shuffle(Cards)
    botCount = 0
    players = []
    #human player
    #myBot = HumanPlayer(Cards[botCount])
    #myBot.playerName = ("HumanPlayer Player "+str(botCount+1))
    #players.append(myBot)
    #ProfMoriartyBot in 100000 games vs a random nuber or aggressive, and random bots, won 31394
    #ProfMoriartyBot in 100000 games vs a passive, aggressive, and random bots, won 2819
    ##
    myBot1 = ProfMoriartyBot(Cards[botCount], botCount)
    myBot1.playerName = ("ProfMoriartyBot Player "+str(botCount+1))
    players.append(myBot1)
    botCount += 1
    myBot2 = ProfMoriartyBot(Cards[botCount], botCount)
    myBot2.playerName = ("ProfMoriartyBot Player "+str(botCount+1))
    players.append(myBot2)
    botCount += 1
    myBot3 = ProfMoriartyBot(Cards[botCount], botCount)
    myBot3.playerName = ("ProfMoriartyBot Player "+str(botCount+1))
    players.append(myBot3)
    botCount += 1
    myBot4 = ProfMoriartyBot(Cards[botCount], botCount)
    myBot4.playerName = ("ProfMoriartyBot Player "+str(botCount+1))
    players.append(myBot4)
    botCount += 1
    ##
    myBot5 = RandomBot(Cards[botCount], botCount)
    myBot5.playerName = ("RandomBot Player "+str(botCount+1))
    players.append(myBot5)
    botCount += 1
    myBot6 = RandomBot(Cards[botCount], botCount)
    myBot6.playerName = ("RandomBot Player "+str(botCount+1))
    players.append(myBot6)
    botCount += 1
    myBot7 = RandomBot(Cards[botCount], botCount)
    myBot7.playerName = ("RandomBot Player "+str(botCount+1))
    players.append(myBot7)
    botCount += 1
    myBot8 = RandomBot(Cards[botCount], botCount)
    myBot8.playerName = ("RandomBot Player "+str(botCount+1))
    players.append(myBot8)
    botCount += 1
    ##
    myBot13 = AggressiveBot(Cards[botCount], botCount)
    myBot13.playerName = ("AggressiveBot Player "+str(botCount+1))
    players.append(myBot13)
    botCount += 1
    myBot14 = AggressiveBot(Cards[botCount], botCount)
    myBot14.playerName = ("AggressiveBot Player "+str(botCount+1))
    players.append(myBot14)
    botCount += 1
    myBot15 = AggressiveBot(Cards[botCount], botCount)
    myBot15.playerName = ("AggressiveBot Player "+str(botCount+1))
    players.append(myBot15)
    botCount += 1
    myBot16 = AggressiveBot(Cards[botCount], botCount)
    myBot16.playerName = ("AggressiveBot Player "+str(botCount+1))
    players.append(myBot16)
    botCount += 1
    ##
    myBot9 = PassiveBot(Cards[botCount], botCount)
    myBot9.playerName = ("PassiveBot Player "+str(botCount+1))
    players.append(myBot9)
    botCount += 1
    myBot10 = PassiveBot(Cards[botCount], botCount)
    myBot10.playerName = ("PassiveBot Player "+str(botCount+1))
    players.append(myBot10)
    botCount += 1
    myBot11 = PassiveBot(Cards[botCount], botCount)
    myBot11.playerName = ("PassiveBot Player "+str(botCount+1))
    players.append(myBot11)
    botCount += 1
    myBot12 = PassiveBot(Cards[botCount], botCount)
    myBot12.playerName = ("PassiveBot Player "+str(botCount+1))
    players.append(myBot12)
    botCount += 1
    ##
    #Random bot in 100000 games vs a random amount of aggressive, passive, and Moriarty bots, won 18120
    #myBot = RandomBot(Cards[botCount])
    #myBot.playerName = ("RandomBot Player "+str(botCount+1))
    #players.append(myBot)
    #AggressiveBot bot in 100000 games vs a random amount of passive, random, and Moriarty bots, won 8291
    #myBot = AggressiveBot(Cards[botCount])
    #myBot.playerName = ("AggressiveBot Player "+str(botCount))
    #players.append(myBot)
    #PassiveBot bot in 100000 games vs a random amount of random amount of aggressive, random, and Moriarty bots won 26345
    #myBot = PassiveBot(Cards[botCount])
    #myBot.playerName = ("PassiveBot Player "+str(botCount))
    #players.append(myBot)
    #botCount += 1
    #while(botCount <16):
     #   botChoice = 1#random.randint(1,3)
      #  if(botChoice == 1):
       #     bot = RandomBot(Cards[botCount])
        #    bot.playerName = ("RandomBot Player "+str(botCount+1))
            #bot = ProfMoriartyBot(Cards[botCount])
            #bot.playerName = ("ProfMoriartyBot Player "+str(botCount+1))
        #elif(botChoice == 2):
         #   bot = AggressiveBot(Cards[botCount])
          #  bot.playerName = ("AggressiveBot Player "+str(botCount+1))
            #bot = ProfMoriartyBot(Cards[botCount])
            #bot.playerName = ("ProfMoriartyBot Player "+str(botCount+1))
        #else:
            #bot = PassiveBot(Cards[botCount])
            #bot.playerName = ("PassiveBot Player "+str(botCount+1))
            #bot = ProfMoriartyBot(Cards[botCount])
            #bot.playerName = ("ProfMoriartyBot Player "+str(botCount+1))
        #players.append(bot)
        #botCount += 1
    #manually add bots here
    #Example:
        #BobThePacifist = PassiveBot(Card[0])
        #BobThePacifist.playerName = "Bob"
        #players.append(BobThePacifist)
    random.shuffle(players)
    newIndex = 0
    for player in players:
        player.updateIndex(newIndex)
        newIndex += 1
    GameOver = False
    dayNumber = 1;
    isDay = True;
    nightEvents = []
    dayEvents = []
    for player in players:
        #print(player)
        player.createRoleList(players)
        
    numberOfDaysWithoutDeath = 0
    while(GameOver == False):
        #print(dayNumber)
        #Count number of still living players
        numberOfDaysWithoutDeath += 1
        for player in players:
            player.updateDeadRoles(players)
            #print(player.playerName + "is a "+player.myClass.className)
            if(player.dead):
                numberOfDaysWithoutDeath = 0
                players.remove(player)
        if(numberOfDaysWithoutDeath > 3):
            #print("No one has died for over 3 days. Game is considered a draw")
            GameOver = True
        #print("")
        todayEvents = []
        if(isDay):
            GameOver = checkWin(players)
            if(GameOver):
                break
                
            #Ask each player what they would like to say durring discussion
            for player in players:
                choice = player.actionOne()
                if choice == 2:
                    role = player.sayRole(player.roleCalled)
                    #print(player.playerName +" claimed they are: "+role)
                    event = (player.playerName +" claimed they are: "+role)
                    for p in players:
                        p.updateSuspects(event)
                        if(p.playerName == "ProfMoriartyBot"):
                            p.trackRoleCounts()
                    todayEvents.append(event)
                elif choice == 3:
                    jaqcus = player.accusePlayer(players)
                    if(jaqcus == -1):
                        #print(player.playerName +" wanted to accuse but changed their mind.")
                        event = (player.playerName +" wanted to accuse but changed their mind.")
                        for p in players:
                            p.updateSuspects(event)
                            if(p.playerName == "ProfMoriartyBot"):
                                p.trackRoleCounts()
                        todayEvents.append(event)
                    else:
                        #print(player.playerName +" wants to accuse: "+str(jaqcus))
                        if(players[jaqcus].botType == "ProfMoriartyBot"):
                            #print("My player was accused")
                            players[jaqcus].updateMySuspicion()
                        event = (player.playerName +" wants to accuse: "+str(jaqcus))
                        for p in players:
                            p.updateSuspects(event)
                            if(p.playerName == "ProfMoriartyBot"):
                                p.trackRoleCounts()
                        todayEvents.append(event)
                else:
                    #print(player.playerName +" did nothing.")
                    event = (player.playerName +" did nothing.")
                    for p in players:
                        p.updateSuspects(event)
                        if(p.playerName == "ProfMoriartyBot"):
                            p.trackRoleCounts()
                    todayEvents.append(event)
            
            #Start Voting phase
            votes = []
            for player in players:
                vote = player.accusePlayer(players)
                #print(player.playerName +" voted player: "+str(vote))
                todayEvents.append(player.playerName +" voted player: "+str(vote))
                if(vote > -1):
                    votes.append(vote)
            if(len(votes) > len(players)/2):
                hangVote = []
                voteResult = max(set(votes), key = votes.count)
                defence = players[voteResult].sayRole(players[voteResult].roleCalled)
                #print(players[voteResult].playerName +" defended themselves by claiming: "+defence)
                todayEvents.append(players[voteResult].playerName +" defended themselves by claiming: "+defence)
                for player in players:
                    if(player != players[voteResult]):
                        vote = player.vote( players[voteResult])
                        hangVote.append(vote)
                hangResult = sum(hangVote)
                if(hangResult > 0):
                    players[voteResult].dead = True
                    numberOfDaysWithoutDeath = 0;
                    #print(players[voteResult].playerName +" is dead. They were a " + players[voteResult].myClass.className)
                    todayEvents.append(players[voteResult].playerName +" is dead. They were a " + players[voteResult].myClass.className)
                    #If player is Seer
                    if(player.myClass.className == "Seer"):
                        player.myClass.deathAbility(players)
                    #If player is tanner
                    if(player.myClass.className == "Tanner"):
                        if(player.dead):
                            tannerWins += 1
                            numberOfWins(players, "Tanner")
                            GameOver = True
                    #If player is Hunter
                    if(player.myClass.className == "Hunter"):
                        target = player.myClass.deathAbility(players, player)
                        players[target].dead = True
                        #print(players[voteResult].playerName +" has shot "+players[target].myClass.className)
                        todayEvents.append(players[voteResult].playerName +" has shot "+players[target].myClass.className)
                        #print(players[target].playerName +" is dead. They where a "+players[target].myClass.className)
                        todayEvents.append(players[target].playerName +" is dead. They where a "+players[target].myClass.className)
            if(GameOver == False):
                GameOver = checkWin(players)
            dayNumber += 1
            isDay = False
            dayEvents.append(todayEvents)
            for player in players:
                player.updateDeadRoles(players)
        else:
            tonightsEvents = []
            for player in players:
                if(player.dead):
                    players.remove(player)
            voteKill = []
            for player in players:
                if(player.myClass.NightAbility):
                    result = player.myClass.nightAbility(players, player)
                    if(player.myClass.team == 2):
                        voteKill.append(result)
                    else:
                        tonightsEvents.append(result)
            if(len(voteKill) > 0):
                voteResult = max(set(voteKill), key = voteKill.count)
                if(players[voteResult].protected == False):
                    players[voteResult].dead = True
                    #print(players[voteResult].playerName+" Has been killed by werewolves.")
                    tonightsEvents.append(players[voteResult].playerName+" Has been killed by werewolves.")
                    if(players[voteResult].myClass.className == "Seer"):
                        players[voteResult].myClass.deathAbility(players)
                    #If player is Hunter
                    if(players[voteResult].myClass.className == "Hunter"):
                        target = players[voteResult].myClass.deathAbility(players, players[voteResult])
                        players[target].dead = True
                        #print(players[voteResult].playerName +" has shot "+players[target].myClass.className)
                        #print(players[target].playerName +" is dead. They where a "+players[target].myClass.className)
                        tonightsEvents.append(players[voteResult].playerName +" has shot "+players[target].myClass.className)
                        tonightsEvents.append(players[target].playerName +" is dead. They where a "+players[target].myClass.className)
                    #else:
                     #   print("Kill target was protected")
            nightEvents.append(tonightsEvents)
            isDay = True
            for player in players:
                player.updateDeadRoles(players)
    counter += 1
    
print("")
print("Town won: "+str(townWins))
print("Town win percentage: "+ str(townWins/numberOfGames))
print("Werewolves won: "+str(werewolfWins))
print("Werewolves win percentage: "+ str(werewolfWins/numberOfGames))
print("Tanner won: "+str(tannerWins))
print("Tanner win percentage: "+ str(tannerWins/numberOfGames))
print("CultLeader won: "+str(cultLeaderWins))
print("CultLeader win percentage: "+ str(cultLeaderWins/numberOfGames))
print("")
print("My Bot has won "+ str(myBotWinCount /4)+" games.")
print("Random Bot has won "+ str(RandomBotWinCounter/ 4)+" games.")
print("Aggressive Bot has won "+ str(AggressiveBotWinCounter/ 4)+" games.")
print("Passive bott has won "+ str(PassiveBotWinCounter / 4)+" games.")
print("Number of Draws: "+ str(Draw))
    
print("")
print("My Bot has won as cult leader "+ str(myBotAsCL /4)+" games.")
print("My Bot has won as WW "+ str(myBotAsWW /4)+" games.")
print("My Bot has won as Tanner "+ str(myBotAsT /4)+" games.")
print("My Bot has won as town "+ str(myBotAsTown /4)+" games.")
    
#Town won: 1444
#Town win percentage: 0.1444
#Werewolves won: 6013
#Werewolves win percentage: 0.6013
#Tanner won: 43
#Tanner win percentage: 0.0043
#CultLeader won: 1635
#CultLeader win percentage: 0.1635

#My Bot has won 1246.75 games.
#Random Bot has won 1155.0 games.
#Aggressive Bot has won 1312.25 games.
#Passive bott has won 981.25 games.
#Number of Draws: 0

## My bot
#My Bot has won as cult leader 143.0 games.
#My Bot has won as WW 764.25 games.
#My Bot has won as Tanner 3.0 games.
#My Bot has won as town 358.5 games.

## Random Bot
#won as cult leader 65.25 games.
#won as WW 827.0 games.
#won as Tanner 0.0 games.
#won as town 247.0 games.

## Aggressive bot
#won as cult leader 107.0 games.
#won as WW 896.25 games.
#won as Tanner 0.0 games.
#won as town 358.75 games.

## Passive bot
#My Bot has won as cult leader 144.75 games.
#My Bot has won as WW 754.5 games.
#My Bot has won as Tanner 0.0 games.
#My Bot has won as town 160.25 games.
    
    
    
    