class Tea:
    
    def __init__(self, size, price = 0.0):
        self.size = size
        self.price = price
    
    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price
    
    def getSize(self):
        return self.size

    def setSize(self):
        self.size = size