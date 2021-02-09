class Person:

    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'hi, this is {self.name}')


person = Person('Ram')
person.talk()
