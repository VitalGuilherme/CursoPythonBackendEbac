#   Polimorfismo

class Animal():
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        return "Au au!"
    
class Gato(Animal):
    def falar(self):
        return "Miau miua!"
    
animais = [Cachorro(), Gato()]

for animal in animais:
    print(animal.falar())