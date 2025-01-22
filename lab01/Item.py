class Item:

    def __init__(self, upc=None, category=None, name=None, price=None):
        self.upc = upc
        if category is not None:
            self.category = category.upper()
        else:
            self.category = None
        if name is not None:
            self.name = name.upper()
        else:
            self.name = None
        self.price = price

    def setUpc(self, upc):
        self.upc = upc 

    def setCategory(self, category):
        self.category = category.upper()

    def setName(self, name):
        self.name = name.upper()

    def setPrice(self, price):
        self.price = price

    def toString(self):
        return ("UPC: {}, Category: {}, Name: {}, Price: ${:.2f}".format(self.upc, self.category, self.name, self.price))
