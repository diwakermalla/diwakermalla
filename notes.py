"""
Attribute in a class:

Public: can be changed outside the class
Protected: can only be changed by the class or a subclass
Private: can only be changed by the class

"""

class MyClass:

    def __init__(self):
        #no underscore is public
        self.my_attribute = None
    
    #single underscore = protected
        self._my_attributemy_attribute = None

    #double underscore = private
        self.__my_attribute = None

"""
self.weakenss is an instance variable which is data stored for everytime
an object is created. I like to imagine an instance variable as a notebook
My friend and I may own the same notebook with a different cover but these
book are two separate instances. If I draw in my notebook, the drawing does
not appear in my friend's copy of the notebook.

You may now be able to guess how a class variable is different from an instance 
variable. A class variable is like having a shared notebook, with all its contents
available to all its notebook owners, i.e. all objects of that class.
"""

# You can create a class variable in Python by adding it outside of the constructor

class My_Class:
    my_class_variable = 0

    def __init__(self):
        #instance variable inside the constructure
        self.my_class_variable = None

"""
Different types of methods: 
1) instance methods (regular use)
2) static methods
3) class methods

Static and class methods do not need object before accessing them.
"""

class My_Class_With_Static_and_Class_Methods:
    
    def instance_method(self):
        print(self)

    @staticmethod
    def static_method():
        print('nothing')

    @classmethod
    def class_method(cls):
        print(cls)

my_object = My_Class_With_Static_and_Class_Methods()
my_object.instance_method()
My_Class_With_Static_and_Class_Methods.static_method()
My_Class_With_Static_and_Class_Methods.class_method()

"""The code in the game demonstrates this usage by using a static method that 
provides the creator of the game in RPGInfo while using a class method to 
allow different authors in the class to say it was created by the author.
"""

"""
Using properties that wrap the getter and setter methods
"""
#The below class using setter and getter without using property
class My_Class_No_Property_Demo:
    def __init__(self):
        self.my_attribute = 0
    
    def get_my_attribute(self):
        return self.my_attribute
    
    def set_my_attribute(self, value):
        self.my_attribute = value
my_object_property_demo = My_Class_No_Property_Demo()
my_object_property_demo.set_my_attribute(1)
print(my_object_property_demo.get_my_attribute())

#The below one uses property instead
class My_Class_Property_Demo:
    def __init__(self):
        self._my_attribute = 0

    @property
    def my_attribute(self):
        return self._my_attribute
    
    @my_attribute.setter
    def my_attribute(self, value):
        self._my_attribute = value




