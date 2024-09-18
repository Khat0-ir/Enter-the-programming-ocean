class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("I am an animal")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print("I am a dog")


dog = Dog("Khat0", "Labrador")
dog.speak()        