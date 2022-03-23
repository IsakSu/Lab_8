from linkedQFile import *

lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
higher = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
nr = [0,1,2,3,4,5,6,7,8,9]
class syntaxException(Exception):
    pass

def readMolekyl(q):
    readAtom(q)


def readAtom(q):
    atom = q.dequeue()
    readHighLetter(atom)
    readLowLetter(atom)

def readHighLetter(q):
    pass

def readNum(q):
    pass

def readLowLetter(q):
    pass

q = LinkedQ()
tmp = input("Mata in molekyl: ")
for i in range(len(tmp)):
    q.enqueue(tmp[i])

while(not q.isEmpty()):
    print(q.dequeue())

if __name__ == "__main__":
    #testprogram
    import unittest
    from linkedQFile import *
    from MolekylSyntax import *

    class TestSyntax(unittest.TestCase):

        def test_peek(self):
            q = LinkedQ()
            q.enqueue("C")
            q.enqueue("h")
            q.enqueue("2")
            self.assertEqual(q.peek(), "h")
            q.dequeue()
            self.assertEqual(q.peek(), "2")

        def test_molekyl(self):
            q=LinkedQ()
            q.enqueue("C")
            q.enqueue("h")
            q.enqueue("3")
            q.enqueue("H")
            q.enqueue("0")
            self.assertEqual(kollaMolekyl(q.dequeue()), "Korrekt syntax")
            self.assertEqual(kollaMolekyl(q.dequeue()), "Fel syntax")

    if __name__ == "__main__":
        #unittest.main()
        tst = "He2"
        print(tst[-1])
