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

def readNumber():
    pass

class Syntaxfel(Exception):
    pass

def kollaMolekyl(atomString):
    queue = LinkedQ()
    for letter in atomString:
        queue.enqueue(letter)
    readLETTER(queue.dequeue())
    if queue.peek() ==


def main():
    queue = LinkedQ()
    molekyl = input("Skriv in en molekyl: ")
    resultat = kollaMolekyl(molekyl)