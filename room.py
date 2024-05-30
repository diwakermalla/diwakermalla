class Room:

    number_of_rooms = 0

    def __init__(self, name):
        self.name = name
        self.description = None
        self.linked_room = {}
        self.character = None
        self.item =  None
        Room.number_of_rooms = Room.number_of_rooms + 1

    def set_description(self, room_description):
        self.description = room_description

    def get_description(self):
        return self.description 

    def set_name(self, room_name):
        self.name = room_name 

    def get_name(self):
        return self.name

    def set_character(self, new_character):
        self.character = new_character
    
    def get_character(self):
        return self.character 

    def get_item(self):
        return self.item
    
    def set_item(self, item_name):
        self.item = item_name        
    
    def describe(self):
       print(self.description) 

    def link_room(self, room_to_link, direction):
       self.linked_room[direction] = room_to_link

    def get_details(self):
        print(self.name)
        print("--------------------")
        print(self.description)

        for direction in self.linked_room:
            room = self.linked_room[direction]
            print("The " + room.get_name() + " is " + direction)

    def move(self, direction):
        print()
        if direction in self.linked_room:
            return self.linked_room[direction]
        else: 
              print('You cannot go that way.')

