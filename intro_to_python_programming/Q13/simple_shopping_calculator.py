class Cart:
    def __init__(self, price1, qty1, price2, qty2, price3, qty3, tax=8.5):
        self.price1 = price1
        self.qty1 = qty1
        self.price2 = price2
        self.qty2 = qty2
        self.price3 = price3
        self.qty3 = qty3
        self.total1 = 0
        self.total2 = 0
        self.total3 = 0
        self.total = 0
        self.tax = tax
        self.calcualteTotal()

    
    def calcualteTotal(self): 
        self.total1 = self.price1 * self.qty1
        self.total2 = self.price2 * self.qty2
        self.total3 = self.price3 * self.qty3
        self.total = self.total1 + self.total2 + self.total3

    def printCart(self):
        print(f"price 1: {self.price1} x {self.qty1} = {int(self.total1)}")
        print(f"price 2: {self.price2} x {self.qty2} = {int(self.total2)}")
        print(f"price 3: {self.price3} x {self.qty3} = {int(self.total3)}")
        print(f"Subtotal: {int(self.total1+self.total2+self.total3)}")
        print(f"Tax (8.5%): {self.tax}")
        print(f"Total: {self.total + (self.total)/100*(self.tax)}")

    @staticmethod
    def input():
        price1 = float(input("Enter price of item 1: "))
        qty1 = int(input("Enter quantity of item 1: "))

        price2 = float(input("Enter price of item 2: "))
        qty2 = int(input("Enter quantity of item 2: "))

        price3 = float(input("Enter price of item 3: "))
        qty3 = int(input("Enter quantity of item 3: "))

        return Cart(price1, qty1, price2, qty2, price3, qty3)

cart = Cart.input()
cart.printCart()
       



