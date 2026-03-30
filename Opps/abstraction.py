from abc import ABC, abstractmethod


class Animal:
    @abstractmethod
    def make_sound(self):
        pass
    

class Lion(Animal):
    def make_sound(self):
        print("Roar !")
        
        
L1 = Lion()
L1.make_sound()