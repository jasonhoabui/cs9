from Tea import Tea

sizeprice = {"S": 12.00, "M": 16.00, "L": 20.00}
toppingprice = {"S": 0.25, "M": 0.50, "L": 0.75}

class SpecialtyTea(Tea):

    def __init__(self, size, name):
        super().__init__(size)
        self.name = name
        self.price = sizeprice[size]

    def getTeaDetails(self):
        return f"SPECIALTY TEA\nSize: {self.size}\nName: {self.name}\nPrice: ${self.price:.2f}\n"
