def integerDivision(n, k):
    if n >= k:
        return 1 + integerDivision(n - k, k)
    return 0

#think about
def collectEvenInts(listOfInt):
    if listOfInt == []:
        return []
    if listOfInt[-1] % 2 != 0:
        listOfInt.pop(-1)
    return collectEvenInts(listOfInt[-1])

def countVowels(someString):
    if someString == "":
        return 0
    if someString[0] in "AEIOUaeiou":
        return 1 + countVowels(someString[1:])
    return countVowels(someString[1:])

def reverseString(s):
    if len(s) == 0:
        return ''
    if len(s) == 1:
        return s
    return reverseString(s[1:]) + s[0]

#think about
def removeSubString(s, sub):
    pass 

print(collectEvenInts([1,2,3,4,5]))