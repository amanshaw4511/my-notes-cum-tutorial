"""
Problem :
    * uncertainties in type of object
    * decisions to be made at runtime regardless of what class to use

Scenario :
    * Pet Shop :
            - intially it sells only Dogs
            - not it wants to sell Cat too

Code Example :
"""

def previously():
    class Dog :
        """ a simple dog class """

        def __init__(self, name):
            self._name = name 

        def speak(self):
            return "Woof!"
    
    def get_pet(pet = "dog"):
        """ the factory method """

        pets = dict( dog=Dog('dog1') )

        return pets[pet]

def now():
    class Dog :
        """ a simple dog class """

        def __init__(self, name):
            self._name = name 

        def speak(self):
            return "Woof!"

    class Cat :
        """ a simple cat class """

        def __init__(self, name):
            self._name = name 

        def speak(self):
            return "Meow!"
    
    def get_pet(pet = "dog"):
        """ the factory method """

        pets = dict( dog=Dog('dog1'), cat=Cat('cat1') )

        return pets[pet]

