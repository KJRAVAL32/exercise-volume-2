class Product:
    def __init__(self, name, code, categeoy, price):
        self.name = name
        self.code = int(code)
        self.categeoy = categeoy
        self.price = int(price)


class Category:
    def __init__(self, name, code, parent='', product=[]):
        self.name = name
        self.code = code
        self.parent = parent
        self.display_name = self._get_display_name()
        self.product = []

    def _get_display_name(self, child_name=''):
        if self.parent:
            if self.parent.parent:
                self.child_name = self.parent.name
                return f"{self.parent._get_display_name(child_name)} > {self.name}"
            else:
                return f"{self.parent.name} > {self.name}"
        else:
            return self.name

    def print_category(self, cat, product):
        print("--------------------------------------------------------------------------")
        for i in cat:
            print(f"Category name: {i.name}, Category code: {i.code}")
            for j in product:
                if i.name == j.categeoy:
                    print(j.name, j.code, j.price)
            print("--------------------------------------------------------------------------")

prod1 = Product("2wheel", "001", "vehicle", 100000)
prod2 = Product("4wheel", "002", "vehicle", 1000000)
prod3 = Product("Truck", "003", "vehicle", 5000000)
prod4 = Product("Kia", "004", "car", 5000000)
prod5 = Product("Hyundai", "005", "car", 5000000)
prod6 = Product("Innova", "006", "car", 5000000)
prod7 = Product("seltos", "007", "Kia", 5000000)
prod8 = Product("sonet", "008", "Kia", 5000000)
prod9 = Product("syros", "009", "Kia", 5000000)
prod10 = Product("Class A", "010", "Petrol", 5000000)
prod11 = Product("Class B", "011", "Petrol", 5000000)
prod12 = Product("Class C", "012", "Petrol", 5000000)
prod13 = Product("BPCL", "013", "Power", 5000000)
prod14 = Product("HPCL", "014", "Power", 5000000)
prod15 = Product("IOCL", "015", "Power", 5000000)
c1 = Category("vehicle", 1, "", [prod1, prod2, prod3])
c2 = Category("car", 2, c1, [prod4, prod5, prod6])
c3 = Category("Kia", 3, c2, [prod7, prod8, prod9])
c4 = Category("Petrol", 4, c3, [prod10, prod11, prod12])
c5 = Category("Power", 5, c4, [prod13, prod14, prod15])
cate = [c1, c2, c3, c4, c5]
products = [prod1, prod2, prod3, prod4, prod5, prod6, prod7, prod8, prod9, prod10, prod11, prod12, prod13, prod14, prod15]
print(c1.display_name)
print(c2.display_name)
print(c3.display_name)
print(c4.display_name)
print(c5.display_name)
cate[0].print_category(cate, products)
