class Product:
    count = 0
    def __init__(self,name,price):
        self.name = name
        self.price = price
        Product.count +=1
        
    @classmethod
    def get_product_count(cls):
        print(f"There are {cls.count} Products")
    
    @staticmethod
    def get_discount(price , discount):
        price(f"total discount is {price - (price * discount/100)}")
        


p1 = Product("Iphone" , 10000)
p2 = Product("Camera" , 3000)

Product.get_product_count()