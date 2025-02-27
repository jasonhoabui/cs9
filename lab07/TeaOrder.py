from Tea import Tea
from CustomTea import CustomTea
from SpecialtyTea import SpecialtyTea

class TeaOrder:

    def __init__(self, distance):
        self.teas = []
        self.distance = distance

    def addTea(self, tea):
        self.teas.append(tea)

    def getOrderDescription(self):
        description = f"******\nShipping Distance: {self.distance} miles\n"
        total_price = 0.0
        
        for i, tea in enumerate(self.teas):
            description += tea.getTeaDetails()
            total_price += tea.getPrice()
            
            if i < len(self.teas) - 1:
                description += "\n----\n"
            else:
                description += "\n----\n"
                
        description += f"TOTAL ORDER PRICE: ${total_price:.2f}\n******\n"
        return description