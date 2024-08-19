class Animal:
    num_of_animal = 0

    def __init__(self):
        pass

class Dog(Animal):
    sound = '멍멍'

    def __init__(self):
        super().__init__()
    
    def bark(self):
        print(f'{self.sound}!')

class Cat(Animal):
    sound = '야옹'

    def __init__(self):
        super().__init__()

    def meow(self):
        print(f'{self.sound}!')

class Pet(Cat, Dog):

    def __init__(self):
        super().__init__()


    def __str__(self):
        return f'애완동물은 {self.sound} 소리를 냅니다.'
    
# dog = Pet()
# print(dog)

cat = Pet()
print(cat)