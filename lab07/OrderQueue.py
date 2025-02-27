class QueueEmptyException(Exception):
    pass

class OrderQueue:
    
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i].distance > self.heapList[i // 2].distance:
                self.heapList[i], self.heapList[i // 2] = self.heapList[i // 2], self.heapList[i]
            i = i // 2

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.maxChild(i)
            if self.heapList[i].distance < self.heapList[mc].distance:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc

    def maxChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            return i * 2 if self.heapList[i * 2].distance > self.heapList[i * 2 + 1].distance else i * 2 + 1

    def addOrder(self, teaOrder):
        self.heapList.append(teaOrder)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def processNextOrder(self):
        if self.currentSize == 0:
            raise QueueEmptyException()
            
        retval = self.heapList[1]
        
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        
        if self.currentSize > 0:
            self.percDown(1)
            
        return retval.getOrderDescription()
