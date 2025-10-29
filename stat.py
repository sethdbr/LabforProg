import matplotlib.pyplot as plt

def bar (Word):
    d = dict()
    for letter in Word:
        d[letter] = d.get(letter,0)+1
        plt.bar(d.keys(), d.values())
    plt.show()

