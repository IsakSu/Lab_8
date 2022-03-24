class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next


class LinkedQ:
    def __init__(self, first = None, last= None):
        self.__first = first
        self.__last = last

    def enqueue(self, value):
        #Köar värden och länkar samman den nya Node med tidigare Node samt ändrar last pointern
        if(self.isEmpty()):
            self.__first = Node(value)
        else:
            if(self.__first.next == None):
                self.__last = Node(value)
                self.__first.next = self.__last
            else:
                self.__last.next = Node(value)
                self.__last = self.__last.next
        return

    def dequeue(self):
        #Tar ut första Node ur kön och ändrar first pointern
        if(not self.isEmpty()):
            temp_value = self.__first.value
            self.__first = self.__first.next
            return temp_value
        else:
            return

    def isEmpty(self):
        #Kollar om första objektet är tomt och därav om länkade listan är tom
        if(self.__first == None):
            return True
        else:
            return False

    def size(self):
        #returnerar storleken av den länkade listan
        counter = 0
        temp_node = self.__first
        while temp_node.next != None:
            temp_node = temp_node.next
            counter += 1
        return counter

    def peek(self):
        if (self.__first != None):
            return self.__first.value
        return None

lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
higher = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
nr = ["0","1","2","3","4","5","6","7","8","9"]
error = False

class molekylException(Exception):
    pass

def readMolekyl(q):
    error = readAtom(q)

    if (q.peek() in nr and error == False):
        error = readNum(q)
    elif not (q.peek() == None):
        error = True;
        #raise molekylException("Fel syntax")
    if(error == False):
        print("Formeln är syntaktiskt korrekt")

    return "Formeln är syntaktiskt korrekt"

def readAtom(q):
    error = False
    if(readHighLetter(q) == True):
        return True

    if not q.peek() in higher and not q.peek() in nr and not q.peek() == None:
        error = readLowLetter(q)
    return error

def readHighLetter(q):
    tempStr = ""
    character = q.dequeue()
    if (character in higher):
        return False
    tempStr += character
    while (not q.peek() == None):
        character = q.dequeue()
        tempStr += character

    print("Saknad stor bokstav vid radslutet " + tempStr)
    return True
    #   raise molekylException("Saknad stor bokstav vid radslutet " + tempStr)

def readNum(q):
    tempList = []
    tempStr = ""
    while (not q.peek() == None):
        character = q.dequeue()
        if (character in nr):
            tempList.append(character)
        else:
            print("Fel syntax")
            return True
            raise molekylException("Fel syntax")

    if int(tempList[0]) == 0:
        #ex: if: atom0  else: atom0123
        if(len(tempList) == 1):
            print("För litet tal vid radslutet")
            return True
            raise molekylException("För litet tal vid radslutet")
        else:
            for i in range(len(tempList)-1):
                tempStr += tempList[i+1]
            print("För litet tal vid radslutet " + tempStr)
            return True
            raise molekylException("För litet tal vid radslutet " + tempStr)

    if (len(tempList) == 1 and int(tempList[0]) == 1):
        #ex: atom1
        print("För litet tal vid radslutet")
        return True
        raise molekylException("För litet tal vid radslutet")
    return False

def readLowLetter(q):
    tempList = []
    character = q.dequeue()
    if (character in lower):
        return False
    print("Saknad liten bokstav vid radslutet")
    return True
    raise molekylException("Saknad liten bokstav vid radslutet")


# if __name__ == "__main__":
#     #testprogram
#     import unittest
#
#     class TestSyntax(unittest.TestCase):
#
#         # def test_peek(self):
#         #     q = LinkedQ()
#         #     q.enqueue("C")
#         #     q.enqueue("h")
#         #     q.enqueue("2")
#         #     self.assertEqual(q.peek(), "C")
#         #     q.dequeue()
#         #     self.assertEqual(q.peek(), "h")
#
#         def test_molekyl(self):
#             q = LinkedQ()
#             ord = input("skriv in Molekyl: ")
#             for bokstav in ord:
#                 q.enqueue(bokstav)
#             self.assertEqual(readMolekyl(q), "Formeln är syntaktiskt korrekt")
#
#     if __name__ == "__main__":
#         unittest.main()

def main():
    from sys import stdin

    q = LinkedQ()
    for line in stdin:
        line = line.strip()
        value = line
        if value == '#':
            break
        elif len(value) != 0:
            for bokstav in value:
                q.enqueue(bokstav)
        readMolekyl(q)


if __name__ == "__main__":
    main()
