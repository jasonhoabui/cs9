''' 

Divide and Conquer Algorithms
subdivide a larger problem into smaller problems
solve each smaller part
combine solutions of smaller sub problems
back into the larger problem

MERGE SORT

break a list into sublists where the size == 1 (considered sorted)
merge each small sorted sublist together to form a sorted larger list
continue to merge sublists back into original lists

'''


def mergesort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        left = alist[:mid]
        right = alist[mid:]
        mergesort(left)
        mergesort(right)
        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                alist[k] = left[i]
                i += 1
            else:
                alist[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            alist[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            alist[k] = right[j]
            j += 1
            k += 1

numList1 = [9,8,7,6,5,4,3,2,1]
numList2 = [1,2,3,4,5,6,7,8,9]
numList3 = []
numList4 = [1,9,2,8,3,7,4,6,5]
numList5 = [5,4,6,3,7,2,8,1,9]
mergesort(numList1)
mergesort(numList2)
mergesort(numList3)
mergesort(numList4)
mergesort(numList5)

assert numList1 == [1,2,3,4,5,6,7,8,9]
assert numList2 == [1,2,3,4,5,6,7,8,9]
assert numList3 == []
assert numList4 == [1,2,3,4,5,6,7,8,9]
assert numList5 == [1,2,3,4,5,6,7,8,9]
