class Product():
    def __init__(self, name, space, price):
        self.name = name
        self.space = space
        self.price = price

# creating instances of the Product class
p1 = Product('refrigerator', 0.60, 1989)

# accessing and printing the products
print(p1.name)
print(p1.space)
print(p1.price)


p2=Product('phone',0.0000055,1500.66)
print(p2.name)
print(p2.space)
print(p2.price)

product_list=[]
product_list.append(Product('refrigerator',0.60, 1989))
product_list.append(Product('phone',0.0000055,1500.66))
product_list.append(Product("TV",0.490,3000))

product_list

#printing information about each product
for product in product_list:
    print(product.name,'-',product.price,'-',product.space)