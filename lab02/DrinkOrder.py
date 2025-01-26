from Beverage import Beverage
from Coffee import Coffee
from FruitJuice import FruitJuice

class DrinkOrder:

    def __init__(self):
        self.drinks = []

    def addBeverage(self, beverage):
        self.drinks.append(beverage)

    def getTotalOrder(self):
        if self.drinks == []:
            return "Order Items:\nTotal Price: $0.00"

        total_drink = "Order Items:\n"
        total_price = 0

        for drink in self.drinks:
            total_drink += f"* {drink.getInfo()}\n"
            total_price += drink.getPrice()

        total_drink += f"Total Price: ${total_price:.2f}"
        return total_drink