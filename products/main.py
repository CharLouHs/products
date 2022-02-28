import os


# 每一個function只做一件事
# 把code寫成function 叫做 refactor 重構


# 讀取檔案
def read_file(filename):
    products = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            name, price = line.strip().split(',')  # 將換行符號和前後空格去掉(split)
            products.append([name, price])
    return products


# 讓使用者輸入
def user_input(products):
    while True:
        name = input('please input the name of product')
        if name == 'q':
            break
        price = input('please input the price of product')
        # p=[]
        # p.append(name)
        # p.append(price)
        price = int(price)
        p = [name, price]
        products.append(p)

    print(products)
    return products


# 印出所有購買紀錄
def print_products(products):
    for product in products:
        print(product[0], '的價格是', product[1])


# 寫入檔案
def write_file(filename, products):
    with open(filename, 'w', encoding='utf-8') as f:  # with的功能就是自動close
        # f.write('商品,價格\n')
        if products[0] != ['商品', '價格']:
            f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')  # 因為+號是字串才能用所以要改成字串型態


def main():
    filename = 'products.csv'
    if os.path.isfile(filename):  # os的file裡面的isfile功能 檢查是否有檔案
        print('yeah! 找到檔案了!!')
        products = read_file(filename)
    else:
        print('找不到檔案。。。')

    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)


main()
