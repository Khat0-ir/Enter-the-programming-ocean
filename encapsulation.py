class TV:
    def __init__(self):
        self.__is_on = False
        self.__volume = 10

    def turn_on(self):
        self.__is_on = True
        print("The TV is now ON")

    def turn_off(self):
        self.__is_on = False
        print("The TV is now OFF")

    def set_volume(self, volume):
        if 0 <= volume <= 100:
            self.__volume = volume
            print(f"Volume set to {self.__volume}")
        else:
            print("Volume must be between 0 and 100")


my_tv = TV()
my_tv.turn_on()
my_tv.set_volume(25)
my_tv.turn_off()