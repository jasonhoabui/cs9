from Apartment import Apartment

def mergesort(apartmentList):
    if len(apartmentList) > 1:
        mid = len(apartmentList) // 2
        left = apartmentList[:mid]
        right = apartmentList[mid:]
        mergesort(left)
        mergesort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                apartmentList[k] = left[i]
                i += 1
            else:
                apartmentList[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            apartmentList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            apartmentList[k] = right[j]
            j += 1
            k += 1

def ensureSortedAscending(apartmentList):
    pass

def getBestApartment(apartmentList):
    pass

def getWorstApartment(apartmentList):
    pass

def getAffordableApartments(apartmentList, budget):
    pass