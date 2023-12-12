# You need to create the 8 classes complete with their attributes and methods.

# class represent person that can place an order in the cafe.
class Customer:
    def __init__(self,name,loyaltyDiscount):
        self.name = name
        self.loyaltyDiscount = loyaltyDiscount
        

# class represent a schedule of items ordered and the cost for a particular customer
class Order:
    def __init__(self,customer):
        self.customer = customer
        self.itemsOrdered = []
        self.cost = 0.0
        
    def addToOrder(Item):
    
    def summariseOrder():

        

# a super class for all food and drink that can be ordered in the cafe
class Item:
    def __init__(self,name,price):
        self.name = name
        self.price = price
        
# a sub class of Item and serves as a super class for all drink items we can purchase.    
class Drink(Item):
    def __init__(self,name,price,size):
        super.__init__(name,price)
        self.size = size
        

#a sub class of Drink to represent a cup of tea that we can order.
class Tea(Drink):
    def __init__(self, name, price, size, flavour):
        super().__init__(name, price, size)
        self.flavour = flavour
    
    def displayDetails():
    


#a sub class of Drink to represent bottled water that we can order.
class MineralWater(Drink):
    def __init__(self, name, price, size, is_carbonated):
        super().__init__(name, price, size)
        self.is_carbonated = is_carbonated
        
    def displayDetails():


#a sub class of Item to represent a tasty item we can order.
class Cake(Item):
    def __init__(self,name,price,sliceSize,type,hasNuts):
        super.__init__(name,price)
        self.sliceSize  = sliceSize
        self.type = type
        self.hasNuts = hasNuts
    def displayDetails():


#a sub class of Item to represent a tasty item we can order.
class Sandwich(Item):
    def __init__(self, name, price, bread_type, filling):
        super().__init__(name, price)
        self.bread_type = bread_type
        self.filling = filling
        self.discount = 0.20
    def displayDetails():

    












def main():
    # Create two customers...
    cust1 = Customer('Harry Palmer', False)
    cust2 = Customer('Bill Preston', True)  # A loyal regular customer

    # Order some items...
    order1 = Order(cust1)
    order1.add_to_order(Tea('Black tea', 2.00, 'large', 'Earl Gray'))
    order1.add_to_order(Sandwich('Club special', 4.50, 'brown', 'chicken'))

    order2 = Order(cust2)
    order2.add_to_order(MineralWater('Evian', 1.50, 'small', False))
    order2.add_to_order(Sandwich('Simple sandwich', 1.50, 'white', 'cheese'))
    order2.add_to_order(Cake('Chocolate dream', 2.30, 'medium', 'chocolate', True))

    # Summarise our orders...
    order1.summarise_order()
    print()
    order2.summarise_order()
    print()


if __name__ == "__main__":
    main()
