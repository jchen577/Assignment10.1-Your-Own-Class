"""
Name: Jacky Chen
Purpose: Creating a class to create NPCs
Assignment: 10.1 Your Own Class
"""
import random

class person():
    __location__ = "Earth"#Makes every instance of person have a location called Earth

    def __init__(self,name,health,enemy = False):#Creates the class object with a name,health, and if they're an enemy
        self.__name__ = name
        self.__health__ = health
        self.__enemy__ = enemy
    
    def get_name(self):#Returns the name
        return self.__name__

    def get_health(self):#Returns the health
        return self.__health__
    
    def damage(self,dmg):#Takes in a damage value and deals that to the health, if it reaches 0, the person "dies"
        self.__health__ = self.__health__ - dmg
        if self.__health__ <= 0:
            return f"{self.__name__} died!"
        else:
            return f"You are left with {self.__health__} health!"

    def get_enemy(self):#Returns if the enemy is an enemy or not
        return self.__enemy__
        
    def get_location(self):#Gets the class variable location
        return self.__location__

    def change_location(self,new_local):#Changes the class variable location of the person object
        self.__location__ = new_local

    def stats(self):#Displays the name, health, and whether the person is an enemy
        print(f"Name: {self.__name__}")
        print(f"Health: {self.__health__}")
        if self.__enemy__ == True:
            print("This is an enemy")
        else:
            print("This is a homie")
        print(f"{self.__name__}'s location: {self.__location__}")
    
    def hit(self,npc):#Gambles if the person hits and it they don't the enemy hits back for damage between 0 to 10
        if npc.get_enemy() == True:
            if random.randint(0,10)%2 != 0:#If it's not even, the person misses
                dmg = random.randint(0,10)
                self.damage(dmg)
                return f"You missed! The enemy retaliates! You take {dmg} damage!"
            else:#Else, the person hits for a damage between 0,10
                dmg = random.randint(0,10)
                npc.damage(dmg)
                return f"You hit! The enemy takes {dmg} damage!"
        else:
            return "Don't hit people randomly!"

    def befriend(self):#Gambles to see whether or not you can befriend the enemy and if you do, self.__enemy__ changes to false
        chance = random.randint(0,10)
        if self.__enemy__ == False:#Checks if the person is already a friend
            return f"{self.__name__} is already a Friend!"
        if chance == 3:#If the random number is 3, the enemy is befriended
            self.__enemy__ == False
            return f"{self.get_name()} befriended!"
        else:#Else, the enemy stays an enemy
            return f"{self.get_name()} stills hates you just as much as before! ...Or does it?"

def main():#Tests each of the different methods and creates multiple npcs
    villager = person("John",16)#Creates the person object with name John and 16 health
    spider = person("Spiderboi",12,True)#Creates person object with name Spiderboi as an enemey with 12 health
    print(villager.hit(spider))#This is using villager to attack/hit the spider using the .hit() method which then calls the .damage() method to reduce one of their healths
    print(f"Is the {villager.get_name()} an enemy? {villager.get_enemy()}!")#Checks if the villager is an enemy or not
    print(f"Villager's name is: {villager.get_name()}")#Prints name of villager
    print(f"{villager.get_name()}'s health is {villager.get_health()}")#Prints health of villager
    spider.stats()#Checks the stats of the spider
    print(spider.befriend())#Tries to befriend the spider
    print(f"{spider.get_name()}'s current location is {spider.get_location()}")#Gets the class variable of the spider which is the location
    spider.change_location("Mars")#Changes the location to Mars
    print(f"{spider.get_name()}'s new location is {spider.get_location()}")#Shows that the location has been changed to Mars

if __name__ == "__main__":
    main()
