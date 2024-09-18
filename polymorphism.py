class Instrument:
    def play(self):
        print("Playing an instrument")


class Piano(Instrument):
    def play(self):
        print("Playing the piano")

class Guitar(Instrument):
    def play(self):
        print("Playing the guitar")


instruments = [Piano(), Guitar()]

for instrument in instruments:
    instrument.play()