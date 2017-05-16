#Backtracking

def BitStrings(n):
    if n == 0:
        return []

    if n == 1:
        return ["0","1"]

    return [digit+bitstring for digit in BitStrings(1) for bitstring in BitStrings(n-1)]

print BitStrings(6)


def rangeToList(k):
    result = []
    for i in range(0,k):
        result.append(str(i))
    return result
def baseKStrings(n,k):
    if n==0: return []
    if n==1: return rangeToList(k)
    return [digit + bitstring for digit in baseKStrings(1,k) for bitstring in baseKStrings(n-1,k)]
    #Above line meaning/..''

print baseKStrings(4,3)
