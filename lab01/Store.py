from Item import Item

class Store:

    def __init__(self):
        self.store_dict = {}

    def addItem(self, item):
        if item.category not in self.store_dict:
            self.store_dict[item.category] = []
        self.store_dict[item.category].append(item)

    def removeItem(self, item):
        for category in self.store_dict:
            for stored_item in self.store_dict[category]:
                if stored_item.upc == item.upc:
                    self.store_dict[category].remove(stored_item)
                    return


    def removeCategory(self, category):
        category = category.upper()
        if category in self.store_dict:
            self.store_dict.pop(category)

    def getItems(self, category):
        category = category.upper()
        if category in self.store_dict:
            result = ""
            items = self.store_dict[category]
            for i in range(len(items)):
                result += items[i].toString()
                if i != len(items) - 1:
                    result += "\n"
            return result
        return ""

    def doesItemExist(self, item):
        for category in self.store_dict:
            for stored_item in self.store_dict[category]:
                if stored_item.upc == item.upc:
                    return True
        return False

    def countDollarItems(self):
        count = 0
        for category in self.store_dict:
            for stored_item in self.store_dict[category]:
                if stored_item.price <= 1:
                    count += 1
        return count

