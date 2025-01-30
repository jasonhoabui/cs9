'''

Python Lists (under the hood)

lists store items in CONTINGUOUS MEMORY 
(one item is located right next to each 
other in memory)

'''


'''

BINARY SEARCH ALGORITHM

useful and performant alg to search for an item
in a list IF THE ITEM IS IN SORTED ORDER

eliminating half the search space for
each iteration is logarithmic (O(log n))

'''


def test_BinarySearchNormal():
    assert binarySearch([1,2,3,4,5,6,7,8,9,10], 5) == True
    assert binarySearch([1,2,3,4,5,6,7,8,9,10], 6) == True
    assert binarySearch([1,2,3,4,5,6,7,8,9,10], 11) == False
    assert binarySearch([1,2,3,4,5,6,7,8,9,10], -5) == False

def test_BinarySearchEmptyList():
    assert binarySearch([], 5) == False

def test_BinarySearchDuplicates():
    assert binarySearch([1,2,2,2,2,3,4,5,6,7,8,9,10], 2) == True
    assert binarySearch([1,2,2,2,2,3,4,5,6,7,8,9,10], 7) == True
    assert binarySearch([1,2,2,2,2,3,4,5,6,7,8,9,10], 0) == False

'''
def binarySearch(intList, int):
    first = 0
    last = len(intList) - 1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2
        if intList[mid] == int:
            found = True
        else:
            if int < intList[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found
'''

def binarySearch(intList, int):
    if len(intList) == 0:
        return False
    mid = len(intList) // 2
    if intList[mid] == int:
        return True
    elif int < intList[mid]:
         return binarySearch(intList[:mid], int)
    return binarySearch(intList[mid+1:], int)