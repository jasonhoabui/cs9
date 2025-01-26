from Beverage import Beverage
from Coffee import Coffee
from FruitJuice import FruitJuice
from DrinkOrder import DrinkOrder


class TestBeverage:

    def test_init(self):
        b1 = Beverage(20, 30)
        b2 = Beverage(19, 30.10)
        assert b1.ounces == 20
        assert b1.price == 30.00
        assert b2.ounces == 19
        assert b2.price == 30.10

    def test_updateOunces(self):
        b1 = Beverage(20, 30)
        b2 = Beverage(19, 30.10)
        b1.updateOunces(21)
        assert b1.ounces == 21
        b2.updateOunces(20)
        assert b2.ounces == 20

    def test_updatePrice(self):
        b1 = Beverage(20, 30)
        b2 = Beverage(19, 30.10)
        b1.updatePrice(25)
        assert b1.price == 25
        b2.updatePrice(30)
        assert b2.price == 30
    
    def test_getOunces(self):
        b1 = Beverage(20, 30)
        b2 = Beverage(19, 30.10)
        assert b1.ounces == 20
        assert b2.ounces == 19
    
    def test_getPrice(self):
        b1 = Beverage(20, 30)
        b2 = Beverage(19, 30.10)
        assert b1.price == 30.00
        assert b2.price == 30.10

    def test_getInfo(self):
        b1 = Beverage(20, 30)
        b2 = Beverage(19, 30.10)
        assert b1.getInfo() == "20 oz, $30.00"
        assert b2.getInfo() == "19 oz, $30.10"

class TestCoffee:

    def test_init(self):
        c1 = Coffee(12, 18.6, "Jason")
        assert c1.ounces == 12
        assert c1.price == 18.60
        assert c1.style == "Jason"

    def test_getInfo(self):
        c1 = Coffee(12, 18.6, "Jason")
        assert c1.getInfo() == "Jason Coffee, 12 oz, $18.60"

class TestFruitJuice:

    def test_init(self):
        d1 = FruitJuice(12, 18.30, ["Apple", "Kiwi", "Banana"])
        assert d1.ounces == 12
        assert d1.price == 18.30
        assert d1.fruits == ["Apple", "Kiwi", "Banana"]

    def test_getInfo(self):
        d1 = FruitJuice(12, 18.30, ["Apple", "Kiwi", "Banana"])
        assert d1.getInfo() == "Apple/Kiwi/Banana Juice, 12 oz, $18.30"

class TestDrinkOrder:

    def test_init(self):
        e1 = DrinkOrder()
        assert type(e1.drinks) == list

    def test_addBeverage(self):
        e1 = DrinkOrder()
        d1 = FruitJuice(12, 18.30, ["Apple", "Kiwi"])
        c1 = Coffee(12, 18.6, "Jason")
        e1.addBeverage(d1)
        e1.addBeverage(c1)
        assert e1.drinks == [d1, c1]

    def test_getTotalOrder(self):
        e1 = DrinkOrder()
        d1 = FruitJuice(12, 18.30, ["Apple", "Kiwi"])
        c1 = Coffee(12, 18.6, "Jason")
        e1.addBeverage(d1)
        e1.addBeverage(c1)
        assert e1.getTotalOrder() == "Order Items:\n* Apple/Kiwi Juice, 12 oz, $18.30\n* Jason Coffee, 12 oz, $18.60\nTotal Price: $36.90"