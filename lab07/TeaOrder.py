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
        order_details = ["******", f"Shipping Distance: {self.distance} miles"]
        order_total = 0.0

        for tea in self.teas:
            order_details.append(tea.getTeaDetails())
            order_total += tea.getPrice()
            order_details.append("\n----")

        order_details.append(f"TOTAL ORDER PRICE: ${order_total:.2f}")
        order_details.append("******")

        return "\n".join(order_details)


ct1 = CustomTea("S", "Black")
ct1.addFlavor("rose")
ct1.addFlavor("cardamom")
st1 = SpecialtyTea("M", "Matcha")
order = TeaOrder(400)
order.addTea(ct1)
order.addTea(st1)

assert order.getOrderDescription() == \
"******\n\
Shipping Distance: 400 miles\n\
CUSTOM TEA\n\
Size: S\n\
Base: Black\n\
Flavors:\n\
\t+ rose\n\
\t+ cardamom\n\
Price: $10.50\n\
\n\
----\n\
SPECIALTY TEA\n\
Size: M\n\
Name: Matcha\n\
Price: $16.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $26.50\n\
******\n"
