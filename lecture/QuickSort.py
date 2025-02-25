def QuickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)
        QuickSortHelper(alist, first, splitpoint - 1)
        QuickSortHelper(alist, splitpoint + 1, last)

def partition(alist, first, last):
   pivotvalue = alist[first]

   leftmark = first + 1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while rightmark >= leftmark and alist[rightmark] >= pivotvalue:
           rightmark = rightmark - 1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

def QuickSort(alist):
    QuickSortHelper(alist, 0, len(alist) - 1)
    



list1 = [1,2,3,4,5,6]
list2 = [2,2,2,2,2,2]
list3 = []
list4 = [6,7,5,3,1]
QuickSort(list1)
assert list1 == [1,2,3,4,5,6]
QuickSort(list2)
assert list2 == [2,2,2,2,2,2]
QuickSort(list3)
assert list3 == []
QuickSort(list4)
assert list4 == [1,3,5,6,7]