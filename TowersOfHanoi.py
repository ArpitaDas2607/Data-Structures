#Chapt3: factorial and Towers of Hanoi using recursion

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(6))
print(factorial(12))

def Print(n):
    if n == 0:
        return 0
    else:
        print n
        Print(n-1)
print(Print(5))


def TowerOfHanoi1(numberOfDiscs, startPeg = 1, endPeg = 3):
    if numberOfDiscs:
        TowerOfHanoi1(numberOfDiscs-1,startPeg,6-startPeg-endPeg)
        print "Move disc %d from peg %d to peg %d"%(numberOfDiscs,startPeg,endPeg)
        TowerOfHanoi1(numberOfDiscs-1,6-startPeg-endPeg,endPeg)

TowerOfHanoi1(numberOfDiscs=5)

print "\n\n\n Now Case II"

def TOH(n, Source, Dest, Aux):
    if n:
        TOH(n-1, Source, Aux, Dest)
        print "Move DISC %d from %s to %s"%(n, Source, Dest)
        TOH(n-1, Aux, Dest, Source)

TOH(7, 'A', 'B', 'C')


def isArrayinSortedOrder(A):
    if len(A) == 1:
        return True
    return A[0] <= A[1] and isArrayinSortedOrder(A[1:])
    #the above statement is true only if 0th element is less than 1st
    #element AND the rest of the list is in sorted order

A = [78,124,987,7602,10000]
print(isArrayinSortedOrder(A))
print(A[1:])
