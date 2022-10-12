# Lab 8 Davide Attebrant och Vira Oetterli
from linkedQFile import LinkedQ

class Syntaxfel(Exception):
    pass

# Tar emot en queue med bara srings som data och ser om den följer syntax.
def readMolekyl(queue):
    readAtom(queue)
    first_character = queue.peek()
    if first_character == None:
        return
    else:
        readNumber(queue)

# Kommer få första karaktären ofiltrerad, andra karaktären kommer den hantera om ej 0-9.
def readAtom(queue):
    # Kollar först bokstav nummer 1 som måste existera
    first_character = queue.peek()
    if type(first_character) == str: #Säkerställer att endast strings matas till readLETTER
        readLETTER(queue)
    else:
        raise Syntaxfel("Saknad stor bokstav vid radslutet")  # Om inte en string
    # Kollar nu om det ev. finns en till bokastav. Om ja så kollar vi att den är liten.
    second_character = queue.peek()
    numberlist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if second_character not in numberlist:
        readLetter(queue)

# Denna kan endast ta emot strings. Kollar att de är stora bokstäver.
def readLETTER(queue):
    character = queue.dequeue()
    if character.isupper():
        return
    else:
        raise Syntaxfel("Saknad stor bokstav vid radslutet")    # Om inte stor bokstav


# Denna kan endast ta emot strings. Kollar att de är små bokstäver.
def readLetter(queue):
    character = queue.dequeue()
    if character.islower():
        return
    else:
        raise Syntaxfel("Saknad stor bokstav vid radslutet")            #Märkligt felmeddelande



# Första är garanterat en siffra (fast i sträng format), övriga tecken kan vara strängar.
def readNumber(queue):
    list = []
    # Vi tar ut första värdet för att se om det är 0.
    if not queue.isEmpty():
        list.append(queue.dequeue())
    if list[0] == '0':
        raise Syntaxfel("För litet tal vid radslutet")
    # Därefter tar vi ut alla övriga värden och ser att de som helhet blir en siffra som är > 1.
    while not queue.isEmpty():
        list.append(queue.dequeue())
    string = ''.join(list)
    try:
        number = int(string)
        if number >= 2:
            return
        else:
            raise Syntaxfel("För litet tal vid radslutet")
    except:
        raise Syntaxfel("För litet tal vid radslutet")


'''test_queue = LinkedQ()
test_queue.enqueue("H")
test_queue.enqueue('h')
#print(test_queue)
test_queue.enqueue("1")
test_queue.enqueue("0")
readMolekyl(test_queue)'''


# Input är en string. Output en linkedQ med alla karaktärer inlagda.
def storeMolekyl(molekylstring):
    queue = LinkedQ()
    for letter in molekylstring:
        queue.enqueue(letter)
    return queue



# Input är en string, output är ett meddelande om ifall den följer syntax eller inte.
def kollaMolekyl(molekylstring):
    queue = storeMolekyl(molekylstring)
    try:
        readMolekyl(queue)
        return "Formeln är syntaktiskt korrekt"
    except Syntaxfel as fel:
        return str(fel) + ' ' + str(queue)



def main():
    string_molekyl = input("Skriv in en molekyl: ")
    resultat = kollaMolekyl(string_molekyl)
    print(resultat)

main()