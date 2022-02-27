products=[]
while True:
    name=input('please input the name of product')
    if name== 'q':
        break
    price=input('please input the price of product')
    #p=[]
    #p.append(name)
    #p.append(price)
    p=[name,price]
    products.append(p)

print(products)