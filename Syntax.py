# Lab 8 Davide Attebrant och Vira Oetterli
from linkedQFile import LinkedQ

def readMolekyl():
    pass

def readAtom():
    pass

def readLETTER():
    pass

def readLetter():
    pass

def readNumberFirst(character):
    character = int(character)
    if character >= 2:
        return
    else
        raise Syntaxfel("För litet tal vid radslutet")

class Syntaxfel(Exception):
    pass


def storeMolekyl(molekylstring):
    queue = LinkedQ()
    for letter in molekylstring:
        queue.enqueue(letter)
    return queue



def kollaMolekyl(molekylstring):
    queue = storeMolekyl(molekylstring)

    try:
        readMolekyl(queue.dequeue())
        return "Formeln är syntaktiskt korrekt"
    except Syntaxfel as fel:
        return str(fel) + " före "              #Komplettera evt detta, se exempel föreläsning

    readLETTER(queue.dequeue())
    if queue.peek() ==


def main():
    queue = LinkedQ()
    molekyl = input("Skriv in en molekyl: ")
    resultat = kollaMolekyl(molekyl)
    print(resultat)