# ----------------------------------- LINKED Q INKOPIERAD ------------------------------------------

# Denna klass skapar noderna.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Denna klass är för själva kön. Den innehåller inga noder, endast två pekare (_first och _last) samt metoder
# för att utföra de metoder som uppgiftsbeskrivningen kräver.
class LinkedQ:

    def __init__(self):
        self._first = None
        self._last = None

    # Lägg till nytt element i slutet av listan
    def enqueue(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self._first = new_node
            self._last = new_node
        else:
            self._last.next = new_node
            self._last = new_node

    # Tar bort och returnerar första elementet
    def dequeue(self):
        if self.size() == 1:
            self.old_first_element = self._first
            self._first = self._first.next
            self._last = None
            return self.old_first_element.data

        elif self.size() > 1:
            self.old_first_element = self._first
            self._first = self._first.next
            return self.old_first_element.data

        else:
            return None

    def isEmpty(self):
        return self._first is None

    def size(self):
        if self._first is None:
            return 0
        else:
            self.inspected_element = self._first
            counter = 1
            while self.inspected_element.next is not None:
                self.inspected_element = self.inspected_element.next
                counter += 1
            return counter

    # ----------------------------------- METODERNA PEEK OCH STRING ------------------------------------------

    def peek(self):
        """Returnerar nästa element i kön om det finns"""
        if self.isEmpty():
            return None
        elif self._first.next is None:
            return None
        elif self._first.next:
            return self._first.next.data

    def str_queue(self):
        """Lägger till nästnästa elementet i en sträng samt alla efterföljande om dessa finns
        Returnerar strängen"""
        first = self._first.next
        string = ""
        while first is not None:
            if first.next:
                string += first.next.data
            first = first.next
        return string


# ------------------------------------- SYNTAXPROGRAMMET -------------------------------------------

class Syntaxfel(Exception):
    pass


def read_molekyl(q, formel):
    """Syntax: <molekyl> ::= <atom> | <atom><num>"""
    read_atom(q, formel)
    read_number(q)


def read_atom(q, formel):
    """Syntax: <atom> ::= <LETTER> | <LETTER><letter>"""
    read_capitol_letter(q, formel)
    read_lowercase_letter(q)


def read_capitol_letter(q, formel):
    """Syntax: <LETTER> ::= A | B | C | ... | Z"""
    capitol = q._first.data
    capitol_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if capitol in capitol_letters:
        return
    raise Syntaxfel("Saknad stor bokstav vid radslutet " + formel)


def read_lowercase_letter(q):
    """Syntax: <letter> ::= a | b | c | ... | z"""
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    if q.peek() is None:
        return
    if q.peek() in lowercase_letters:
        q.dequeue()  # Plockar ut capitol letter för att kunna peeka tecknet efter lowercase letter
        return
    try:
        int(q.peek())  # Om tecknet är en siffra istället för lower case letter följer detta syntaxen
        return
    except ValueError:
        raise Syntaxfel("Fel tecken vid radslutet " + q.str_queue())  # tex: !#".?


def read_number(q):
    """Syntax: <num> ::= 2 | 3 | 4 | ..."""
    if q.peek() is None:
        return
    if q.peek() == "0":
        raise Syntaxfel("För litet tal vid radslutet " + q.str_queue())
    if q.peek() == "1":
        q.dequeue()  # Plockar ut föregående tecken för att kunna peeka tecknet efter ettan
        second_number = q.peek()
        if second_number is None:
            raise Syntaxfel("För litet tal vid radslutet " + q.str_queue())
    try:
        int(q.peek())
    except ValueError:
        raise Syntaxfel("Fel tecken vid radslutet " + q.str_queue())


# ------------------------------------- KÖR SYNTAXPROGRAMMET -------------------------------------------

def kolla_formel(formel):
    """Skapar kön och testar syntaxen
    Returnerar sträng med korrekt- eller felmeddelande"""
    q = LinkedQ()
    for symbol in formel:
        q.enqueue(symbol)  # köar alla tecken i inmatad formel som en länkad kö
    try:
        read_molekyl(q, formel)
        return "Formeln är syntaktiskt korrekt"
    except Syntaxfel as fel:
        return str(fel)


def main():
    """Anpassat main-program för Kattis"""
    rad = input()
    while rad != "#":
        print(kolla_formel(rad))
        rad = input()


main()

# ----------------------------------- TEST FÖR SYNTAXPROGRAM ------------------------------------------


