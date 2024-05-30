"""
Exercise: 
Text-based game where you have three rooms in a house. The rooms are dining, kitchen and living. 
In each house, there is a character. One is friendly, the other is an enemy and the last one is neither friendly or enemy. 
You can talk to the characters, fight with the enemy, or hug a friendly character.
You can store items in a player's backpack and there will be a few items in each room. 
You can take items from the current room and put it in the backpack. You can remove items from the backpack and put it in the room. 
The backpack can only hold 3 items. You will be limited to fight with the items. 
Once the player beats all the enemies, the game will be won.
"""
from RPGInfo import RPGInfo
from room import Room

spooky_castle = RPGInfo('Spooky Castle') #static method can only be accessed by 
spooky_castle.welcome()
RPGInfo.info()

RPGInfo.author = 'Raspberry pi foundation'
RPGInfo.credit()

kitchen = Room('Kitchen')
kitchen.set_description('Stinky place where you eat!')

dining_hall = Room('Dining Hall')
dining_hall.set_description('Place you gather and eat with family')

ballroom = Room('Ballroom')
ballroom.set_description('Decorated place with lots of lights')

kitchen.link_room(dining_hall, 'south')
dining_hall.link_room(kitchen, 'north')
dining_hall.link_room(ballroom, 'west')
ballroom.link_room(dining_hall, 'east')

current_room = kitchen

while True:
    current_room.get_details()
    
    command = input('>')
    current_room = current_room.move(command)    

#git change something to push to a different branch
#change comments to push to test
#add more comments to push to test
#add comments to push to main