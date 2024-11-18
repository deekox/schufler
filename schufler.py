import os
import random



# functionality:
#   1) show a place on a guitar neck (in: string, fret)
#   2) show a note on a staff (in: note value 0-E0, 1-F0, ...)
#   3) 

# note values on strings [E3, B2, G2, D2, A1, E1]
tune = [0, 7, 3, 10, 5, 0]


class Note:
    def __init__(self):
        "low E on guitar"
        self.value = 0


def getNoteName(value, isSharp):
    if value < 0:
        value = -value
    value = value % 12
#    print(value)
#             0    1    2     3    4     5    6     7    8    9     10   11  
    sharp = ["E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#"]
    flat =  ["E", "F", "Gb", "G", "Ab", "A", "Bb", "B", "C", "Db", "D", "Eb"]

    if isSharp:
        return sharp[value]
    return flat[value]

def drawHeader():
    print('               o           o           o           o                o o')

def drawString(markFret):
    for a in range(12):
        if markFret == 0 and a == 0:
            print("X-----", end="")
        elif markFret - 1 == a:
            print("|--X--", end="")
        else:
            print('|-----', end="")
    print('|')


def getFret(note, string):
    string = string % 6
    fret = (note + tune[string]) % 12
    print(f"fret: {fret}")




for s in range(6):
    print(f"string: {getNoteName(tune[s], True)}")
    for n in range(14):
        print(f"fret: {n}, note: {getNoteName(tune[s] + n, True)}")

    drawHeader()
    for a in range(12):
        drawString(a)
    # drawString(1, 2)

    # val = random.randrange(100)
    # sharp = random.randrange(2)
    # note = getNoteName(val, sharp == 0)
    # print(f'{val} -- {note}')    



#os.system('cls')