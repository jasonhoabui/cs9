'''
INSERTION SORT

we want to work left-to-right and insert unsorted elements
into the sorted right portion of the list



'''


def InsertSort(aList):
    for index in range(1, len(aList)):
        currentValue = aList[index]
        position = index
        #shift elements to make room for insertion
        while position > 0 and aList[position - 1] > currentValue:
            aList[position] = aList[position - 1]
            position = position - 1

        #insert element in appropriate place
        aList[position] = currentValue

list1 = [1,2,3,4,5,6]
list2 = [2,2,2,2,2,2]
list3 = []
list4 = [6,7,5,3,1]
InsertSort(list1)
assert list1 == [1,2,3,4,5,6]
InsertSort(list2)
assert list2 == [2,2,2,2,2,2]
InsertSort(list3)
assert list3 == []
InsertSort(list4)
assert list4 == [1,3,5,6,7]