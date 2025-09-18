class Product:
    def __init__(self, name, code, categeoy, price):
        self.name = name
        self.code = int(code)
        self.categeoy = categeoy
        self.price = int(price)


class Category:
    def __init__(self, name, code, parent=''):
        self.name = name
        self.code = code
        self.parent = parent
        self.display_name = self._get_display_name()

    def _get_display_name(self, child_name=''):
        if self.parent:
            if self.parent.parent:
                self.child_name = self.parent.name
                return f"{self.parent._get_display_name(child_name)} > {self.name}"
            else:
                return f"{self.parent.name} > {self.name}"
        else:
            return self.name

    def print_category(self, cate, products):
        print("--------------------------------------------------------------------------")
        for i in cate:
            print(f"Category name: {i.name}, Category code: {i.code}")
            for j in products:
                if i.name == j.categeoy.name:
                    print(j.name, j.code, j.price)
            print("--------------------------------------------------------------------------")


c1 = Category("vehicle", 1)
c2 = Category("car", 2, c1)
c3 = Category("Kia", 3, c2)
c4 = Category("Petrol", 4, c3)
c5 = Category("Power", 5, c4)
cate = [c1, c2, c3, c4, c5]
print(c1.display_name)
print(c2.display_name)
print(c3.display_name)
print(c4.display_name)
print(c5.display_name)
products = [
    Product("2wheel", "001", c1, 100000),
    Product("4wheel", "002", c1, 1000000),
    Product("Truck", "003", c1, 5000000),
    Product("Kia", "004", c2, 5000000),
    Product("Hyundai", "005", c2, 5000000),
    Product("Innova", "006", c2, 5000000),
    Product("seltos", "007", c3, 5000000),
    Product("sonet", "008", c3, 5000000),
    Product("syros", "009", c3, 5000000),
    Product("Class A", "010", c4, 5000000),
    Product("Class B", "011", c4, 5000000),
    Product("Class C", "012", c4, 5000000),
    Product("BPCL", "013", c5, 5000000),
    Product("HPCL", "014", c5, 5000000),
    Product("IOCL", "015", c5, 5000000)
]
cate[0].print_category(cate, products)

