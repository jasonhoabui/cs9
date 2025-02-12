'''

ORDERED LINKED LISTS

similar to an unordered linked list except the nodes are ordered with respect to each other


QUADRATIC SORTING ALGORITHMS

linear search starting at the beginning and check every element in the list
does not require elements to be sorted

binary search check middle, left or right sub lists
does require elements to be sorted

how do we sort elements?

BUBBLE SORT 

idea: it will make several passes through the list and swap adjacent elements to ensure
the largest element ends up at the end of the list (assume we are sorting in ascending order, least-to-greatest)


'''




def bubbleSort(aList):
    for passnum in range(len(aList) - 1, 0, -1):
        #print("passnum ", passnum)
        for i in range(passnum):
            #print("index ", i)
            if aList[i] > aList[i + 1]:
                # swap (bubble up!)
                temp = aList[i]
                aList[i] = aList[i + 1]
                aList[i+1] = temp
            #print(aList)





def test_bubbleSort():
    list1 = [1,2,3,4,5,6]
    list2 = [2,2,2,2,2,2]
    list3 = []
    list4 = [6,7,5,3,1]
    bubbleSort(list1)
    assert list1 == [1,2,3,4,5,6]
    bubbleSort(list2)
    assert list2 == [2,2,2,2,2,2]
    bubbleSort(list3)
    assert list3 == []
    bubbleSort(list4)
    assert list4 == [1,3,5,6,7]