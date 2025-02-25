'''

QUICKSORT and TREES

can improve runtimes to O(n log n) in a typical case
but can lead to O(n ^ 2) in the worse case scenario

can sort a list by subdividing the list based on PIVOT value
place elements < pivot to the left side of the list
place elements > pivot to the right side of the list
recurse for each left / right portion
when sub list sizes == 1, then the entire list is sorted

how do we partition the list into left / right sublists?

choose pivot, 1st element at index[0] because the elements are random
find an element in the left side (using leftmark index starting
at the beginning of the list just past the pivot that will move 
right) that's out of place (> pivot)

find an element in the right side (using leftmark index starting
at the beginning of the list just past the pivot that will move 
left) that's out of place (< pivot)

swap out of place elements with each other
we are putting them in the correct side of the list
continue doing this until rightmark index < leftmark index

swap the pivot element with rightmark -> putting the pivot element in the correct place
'''