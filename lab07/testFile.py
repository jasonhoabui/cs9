from Tea import Tea
from CustomTea import CustomTea
from SpecialtyTea import SpecialtyTea
from TeaOrder import TeaOrder
from OrderQueue import OrderQueue, QueueEmptyException

def test_Tea():
    tea = Tea("M")
    assert tea.getSize() == "M"
    assert tea.getPrice() == 0.0
    
    tea.setSize("L")
    tea.setPrice(5.0)
    assert tea.getSize() == "L"
    assert tea.getPrice() == 5.0

def test_CustomTea():
    ct = CustomTea("S", "Green")
    assert ct.getSize() == "S"
    assert ct.getBase() == "Green"
    assert ct.getPrice() == 10.00
    
    expected = "CUSTOM TEA\nSize: S\nBase: Green\nFlavors:\nPrice: $10.00\n"
    assert ct.getTeaDetails() == expected
    
    ct.addFlavor("lemon")
    ct.addFlavor("ginger")
    assert ct.getPrice() == 10.50 
    
    expected = "CUSTOM TEA\nSize: S\nBase: Green\nFlavors:\n\t+ lemon\n\t+ ginger\nPrice: $10.50\n"
    assert ct.getTeaDetails() == expected
    
    ct_large = CustomTea("L", "Black")
    assert ct_large.getPrice() == 20.00
    
    ct_large.addFlavor("honey")
    assert ct_large.getPrice() == 20.75 

def test_SpecialtyTea():
    st = SpecialtyTea("M", "Earl Grey")
    assert st.getSize() == "M"
    assert st.getPrice() == 16.00
    
    expected = "SPECIALTY TEA\nSize: M\nName: Earl Grey\nPrice: $16.00\n"
    assert st.getTeaDetails() == expected
    
    st_small = SpecialtyTea("S", "Matcha")
    assert st_small.getPrice() == 12.00

def test_TeaOrder():
    ct = CustomTea("S", "Black")
    ct.addFlavor("mint")
    st = SpecialtyTea("L", "Chai")
    
    order = TeaOrder(250)
    order.addTea(ct)
    order.addTea(st)
    
    order_desc = order.getOrderDescription()
    assert "Shipping Distance: 250 miles" in order_desc
    assert "CUSTOM TEA" in order_desc
    assert "Size: S" in order_desc
    assert "Base: Black" in order_desc
    assert "mint" in order_desc
    assert "SPECIALTY TEA" in order_desc
    assert "Size: L" in order_desc
    assert "Name: Chai" in order_desc
    assert "TOTAL ORDER PRICE: $30.25" in order_desc 

def test_OrderQueue():
    order1 = TeaOrder(100)
    order1.addTea(CustomTea("S", "Green"))
    
    order2 = TeaOrder(300)
    order2.addTea(SpecialtyTea("M", "English Breakfast"))
    
    order3 = TeaOrder(200)
    order3.addTea(CustomTea("L", "Oolong"))
    
    queue = OrderQueue()
    queue.addOrder(order1)
    queue.addOrder(order2)
    queue.addOrder(order3)
    
    desc1 = queue.processNextOrder()
    assert "Shipping Distance: 300 miles" in desc1
    assert "English Breakfast" in desc1
    
    desc2 = queue.processNextOrder()
    assert "Shipping Distance: 200 miles" in desc2
    assert "Oolong" in desc2
    
    desc3 = queue.processNextOrder()
    assert "Shipping Distance: 100 miles" in desc3
    assert "Green" in desc3
    
    with pytest.raises(QueueEmptyException):
        queue.processNextOrder()