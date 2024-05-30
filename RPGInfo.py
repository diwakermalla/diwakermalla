class RPGInfo:

    #create a class variable to welcome your players
    #When you initialize the credit, you will initialize it as spooky castle. Provide a message that welcomes players to the game.
    #You want to give credit by quoting the author.
    #You want to credit the company raspberry pi foundation.
    
    author = 'anonymous'

    def __init__(self, game_title):
        self.title = game_title
    
    def welcome(self):
        print('Welcome to the ' + self.title)

    @staticmethod
    def info():
        print('Made using the OOP RPG game creator (c) me')

    @classmethod
    def credit(cls):
        print('Created by '+ cls.author)    