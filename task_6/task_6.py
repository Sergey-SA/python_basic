class Animal:
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
cat.voice()

dog = Dog()
dog.voice()

tiger = Tiger()
tiger.voice()