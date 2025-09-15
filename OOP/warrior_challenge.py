import random
import math

"""
Sam attacks Paul and deals 9 damage
Paul is down to 10 health
Paul attacks Sam and deals 7 damage
Sam is down to 7 health
Sam attacks Paul and deals 19 damage
Paul is down to -9 health
Paul has Died and Sam is Victorious
Game over
"""

# Warrior & Battle Class
# Attributes
# Warriors will have names, health (death), attack and block maximms
# Capabilities
# They will have the capabilities to attack and block random amounts
# Attributes
# Warriors will have names, health (death), attack and block maximms
# Capabilities
# They will have the capabilities to attack and block random amounts
# Attributes
# Warriors will have names, health (death), attack and block maximms
# Capabilities
# They will have the capabilities to attack and block random amounts
# Attack -> random() - 0.0 to 1.0 * maxAttack + .5
# Block will use random() 
# Battle Class - capability of looping until 1 warrior dies
# Warriors will each get a turn to attack each other 
# Function to handle the attack phase
# Function gets two warriors
# 1 warrior attacks the other
# Attacks and blocks be integers


class Warrior:
    def __init__(self, name="Warrior", health=0, attackMax=0, blockMax=0):
        self.name = name
        self.health = health
        self.attackMax = attackMax
        self.blockMax = blockMax
     
    def attack(self):
        attack_amount = self.attackMax * (random.random() + .5)
        return attack_amount

    def block(self):
        block_amount = self.blockMax * (random.random() + .5)
        return block_amount

# creating a battle class
# No need to initialize, will work great as a utility class
# with capabilities to loop and have warriors fight against each other

class Battle:

    def startFight(self, warrior1, warrior2):
        while True:
            if self.getAttackResult(warrior1, warrior2) == "Game Over":
                print("Game Over")
                break
            if self.getAttackResult(warrior2, warrior1) == "Game Over":
                print("Game Over")
                break

    # doesn't require the use of self
    # everything that the function needs will be passed inside of the 
    # attributes above
    # class method - not tied to any type of object
    # has no need to refer to self, all the info it is getting is going
    # to be passed in the attributes - mark as static method
    # static method is a capability of a class
    """
    Any time you create a method or you have an attribute that isn't
    directly related to a real world object that you are trying to 
    model in that situation that thing should be static 
    """
    
    @staticmethod
    def getAttackResult(warriorA, warriorB):
        warriorA_attack_amount = warriorA.attack()
        warriorB_block_amount = warriorB.block()
        damage2_warriorB = math.ceil(warriorA_attack_amount - warriorB_block_amount)
        warriorB.health = warriorB.health - damage2_warriorB

        print("{} attacks {} and deals {} damage"
              .format(warriorA.name, warriorB.name, damage2_warriorB))
        print("{} is down to {} health".format(warriorB.name, warriorB.health))

        if warriorB.health <= 0:
            print("{} has Died and {} is Victorious".format(warriorB.name, warriorA.name))
            return "Game Over"
        else:
            return "Fight Again"

def main():
    hiticus = Warrior("Hiticus", 50, 20, 10)
    alfonso = Warrior("Alfonso", 50, 20, 10)

    battle = Battle()

    battle.startFight(hiticus, alfonso)

main()

