def getCount():
    print('count =', Animal.count)

class Animal:
    count = 0

    def __init__(self):
        Animal.count += 1

    def voice(self):
        pass

class Cat(Animal):
    def voice(self):
        print('may')

class Dog(Animal):
    def voice(self):
        print('gav')

class Tiger(Animal):
    def voice(self):
        print('rrrr')

cat = Cat()
dog = Dog()
tiger = Tiger()

getCount()