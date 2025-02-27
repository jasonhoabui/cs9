from Tea import Tea

sizeprice = {"S": 10.00, "M": 15.00, "L": 20.00}
toppingprice = {"S": 0.25, "M": 0.50, "L": 0.75}

class CustomTea(Tea):

    def __init__(self, size, base):
        super().__init__(size)
        self.base = base
        self.flavors = []
        self.price = sizeprice[size]

    def setBase(self, base):
        self.base = base

    def getBase(self):
        return self.base

    def addFlavor(self, flavor):
        self.flavors.append(flavor)
        self.price += toppingprice[self.size]

    def getTeaDetails(self):
        details = f"CUSTOM TEA\nSize: {self.size}\nBase: {self.base}\nFlavors:\n"
        for flavor in self.flavors:
            details += f"\t+ {flavor}\n"
        details += f"Price: ${self.price:.2f}\n"
        return details