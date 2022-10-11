# Lab 8 Davide Attebrant och Vira Oetterli
from linkedQFile import LinkedQ

class Syntaxfel(Exception):
    pass

def readMolekyl(queue):
    readAtom(queue)
    if type(queue.peek()) is not None:
        readNumber(queue)


def readAtom(queue):
    readLETTER(queue)
    # Kollar först bokstav nummer 1 som måste existera
    first_object = queue.peek()
    print(first_object)
    if type(queue.peek) == str: #Säkerställer att endast strings matas till readLETTER
        readLetter(queue)
    else:
        raise Syntaxfel("Saknad stor bokstav vid radslutet" + str(queue))  # Om inte en string
    # Kollar nu om det ev. finns en till bokastav
    if type(queue.peek) == str:
        readLetter(queue)

# Denna kan endast ta emot strings. Kollar att de är stora bokstäver.
def readLETTER(queue):
    character = queue.dequeue()
    if character.isupper():
        return
    else:
        raise Syntaxfel("Saknad stor bokstav vid radslutet" + str(queue))    # Om inte stor bokstav


# Denna kan endast ta emot strings. Kollar att de är små bokstäver.
def readLetter(queue):
    character = queue.dequeue()
    if character.islower():
        return
    else:
        raise Syntaxfel("Saknad stor bokstav vid radslutet" + str(queue))            #Märkligt felmeddelande

test_queue = LinkedQ()
test_queue.enqueue("h")
test_queue.enqueue("H")
#print(test_queue)
#test_queue.enqueue("H")
readLETTER(test_queue)

def readNumber(queue):
    list = []
    while not queue.isEmpty():
        list.append(queue.dequeue())
    try:
        number = 0
        for element in list:
            number =+ int(element)
        if number >= 2:
            return
        else:
            raise Syntaxfel("För litet tal vid radslutet" + str(queue))
    except:
        raise Syntaxfel("För litet tal vid radslutet" + str(queue))





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
        return str(fel) + str(queue)



def main():
    queue = LinkedQ()
    molekyl = input("Skriv in en molekyl: ")
    resultat = kollaMolekyl(molekyl)
    print(resultat)