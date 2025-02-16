def SelectionSort(aList):
    for fillslot in range(len(aList) -1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            if aList[location] > aList[positionOfMax]:
                positionOfMax = location

        #swap the largest element into the correct place
        temp = aList[fillslot]
        aList[fillslot] = aList[positionOfMax]
        aList[positionOfMax] = temp


list1 = [1,2,3,4,5,6]
list2 = [2,2,2,2,2,2]
list3 = []
list4 = [6,7,5,3,1]
SelectionSort(list1)
assert list1 == [1,2,3,4,5,6]
SelectionSort(list2)
assert list2 == [2,2,2,2,2,2]
SelectionSort(list3)
assert list3 == []
SelectionSort(list4)
assert list4 == [1,3,5,6,7]