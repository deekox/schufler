import os
import random



class Note:
    def __init__(self):
        "low E on guitar"
        self.value = 0


def getNoteName(value, isSharp):
    if value < 0:
        value = -value
    value = value % 12
#    print(value)
    sharp = ["E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#"]
    flat = ["E", "F", "Gb", "G", "Ab", "A", "Bb", "B", "C", "Db", "D", "Eb"]

    if isSharp:
        return sharp[value]
    return flat[value]



for i in range(100):
    val = random.randrange(100)
    sharp = random.randrange(2)
    note = getNoteName(val, sharp == 0)
    print(f'{val} -- {note}')    


#os.system('cls')