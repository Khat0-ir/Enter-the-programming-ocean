class Car:
    def __init__(self,color,model):
        self.color = color
        self.model = model

    def drive(self):
        print(self.model,' is driving with color',self.color)    



car1 = Car('red','benz')

car2 = Car('white','bmw')


car1.drive()
car2.drive()


# class Car:
#     def __init__(self, color, model):
#         self.color = color
#         self.model = model

#     def drive(self):
#         print("The car is driving")


# car1 = Car("red", "sedan")
# car2 = Car("blue", "SUV")

# car1.drive()  
# car2.drive() 