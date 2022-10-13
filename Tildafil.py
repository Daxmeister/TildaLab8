# Lab 8 Davide Attebrant och Vira Oetterli

# Denna klass skapar noderna.
class Node():

    def __init__(self, data):
        self.data = data
        self.next = None

# Denna klass är för själva kön. Den innehåller inga noder, endast två pekare (_first och _last) samt metoder
# för att utföra de metoder som uppgiftsbeskrivningen kräver.
class LinkedQ():

    def __init__(self):
        self._first = None
        self._last = None

    # Lägg till nytt element i slutet av listan
    def enqueue(self, int):
        new_node = Node(int)        # Skapar ny nod med datan.
        if self.isEmpty():          # Om det är första elementet. Då blir den både sist och först!
            self._first = new_node
            self._last = new_node
        else:                       # Nu ska bara last pekas om. First pekar kvar på första noden.
            self._last.next = new_node      # Sista noden i listan ska peka på den "nya sista" noden.
            self._last = new_node

    # Tar bort och returnerar första elementet
    def dequeue(self):
        if self.size() == 1:
            self.old_first_element = self._first    # Skapar ny pekare som kommer ihåg vårt första element.
            self._first = self._first.next          # Kommer peka på None
            self._last = None                       # Kommer peka på None. Detta är det speciella med att ha 1 i listan.
            return self.old_first_element.data

        elif self.size() > 1:
            self.old_first_element = self._first
            self._first = self._first.next
            return self.old_first_element.data

        else:
            return None

    # Returnerar True om listan är tom.
    def isEmpty(self):
        return self._first == None

    # Returnerar hur långa linked list är.
    def size(self):
        if self._first == None:
            return 0
        else:
            self.inspected_element = self._first
            counter = 1
            while self.inspected_element.next != None:  # Denna kollar om vårt element är det sista.
                self.inspected_element = self.inspected_element.next # Vi går till nästa element i listan.
                counter += 1
            return counter

    def peek(self):
        if self._first is not None:
            return self._first.data
        else:
            return None

    def show_first(self):
        print(self._first.data)

    def show_last(self):
        print(self._last.data)

    def __str__(self):
        list = []
        pekare = self._first
        while pekare != None:
            list.append(pekare.data)
            pekare = pekare.next
        string = ''.join(map(str, list))
        return string


'''q = LinkedQ()
q.enqueue("pongis")
q.enqueue(13)
q.enqueue("tip")
print(q)'''


class Syntaxfel(Exception):
    pass

# Tar emot en queue med bara strings som data och ser om den följer syntax.
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
        raise Syntaxfel("Saknad stor bokstav vid radslutet ")  # Om inte en string
    # Kollar nu om det ev. finns en till bokastav. Om ja så kollar vi att den är liten.
    second_character = queue.peek()
    numberlist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if second_character not in numberlist and second_character is not None:
        readLetter(queue)

# Denna kan endast ta emot strings. Kollar att de är stora bokstäver.
def readLETTER(queue):
    character = queue.dequeue()
    if character.isupper():
        return
    else:
        raise Syntaxfel("Saknad stor bokstav vid radslutet " + character)    # Om inte stor bokstav


# Denna kan endast ta emot strings. Kollar att de är små bokstäver.
def readLetter(queue):
    character = queue.dequeue()
    if character.islower():
        return
    else:
        raise Syntaxfel("Saknad stor bokstav vid radslutet ")



# Första är garanterat en siffra (fast i sträng format), övriga tecken kan vara strängar.
def readNumber(queue):
    list = []
    # Vi tar ut första värdet för att se om det är 0.
    if not queue.isEmpty():
        list.append(queue.dequeue())
    if list[0] == '0':
        raise Syntaxfel("För litet tal vid radslutet ")
    # Därefter tar vi ut alla övriga värden och ser att de som helhet blir en siffra som är > 1.
    while not queue.isEmpty():
        list.append(queue.dequeue())
    string = ''.join(list)
    try:
        number = int(string)
        if number >= 2:
            return
        else:
            raise Syntaxfel("För litet tal vid radslutet ")
    except:
        raise Syntaxfel("För litet tal vid radslutet ")

# ----------------------------------------Kör Programmet -------------------------------------------------------

# Input är en string. Output en linkedQ med alla karaktärer inlagda.
def storeMolekyl(molekylstring):
    queue = LinkedQ()
    for character in molekylstring:
        queue.enqueue(character)
    return queue



# Input är en string, output är ett meddelande om ifall den följer syntax eller inte.
def kollaMolekyl(molekylstring):
    queue = storeMolekyl(molekylstring)
    try:
        readMolekyl(queue)
        return "Formeln är syntaktiskt korrekt"
    except Syntaxfel as fel:
        return str(fel) + str(queue)


# Kör själva programmet
def main():
    string_molekyl = input()
    while string_molekyl != '#':
        print(kollaMolekyl(string_molekyl))
        string_molekyl = input()

main()




