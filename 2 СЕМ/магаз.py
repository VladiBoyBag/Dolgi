from datetime import datetime


class Shop:
    def __init__(self, products, prices, quantity, name):
        self.products = products
        self.prices = prices
        self.quantity = quantity
        self.name = name
        self.shop, self.product, self.count, self.save_check = None, None, None, None

    def __str__(self):
        return f"{self.__class__.__name__}"

    def user_buy(self, product_name, count, user_name, save_check=False):
        index = 0
        while product_name != self.products[index]:
            index += 1

        if count > 0:
            if self.quantity[index] >= count:
                self.quantity[index] -= count
            else:
                print("В магазине меньшее кол-во товара, что Вы просите")
            if save_check is True:
                date_and_time = str(datetime.today()).split()
                date = date_and_time[0]
                time = date_and_time[1][:8]
                time = [x for x in time]
                for _ in time:
                    if _ == ':':
                        time[time.index(_)] = '-'
                time = ''.join(time)

                with open(f"{user_name}_{date}_{time}.txt", "w", encoding='utf-8') as file:
                    file.write(f'купленный товар: {product_name}\nкол-во товара: {count}\nмагазин: {self.name}')
                file.close()
        else:
            print("Не вижу смысла в Вашей покупке")

    def counting(self):
        for i in range(len(self.quantity)):
            if self.quantity[i] == 0:
                del self.products[i]
                del self.prices[i]

    def find_product(self, product_name, should_i_print=True, count=0):
        useful_shops = []
        for i in shops:
            for j in range(len(i.products)):
                if (i.products[j] == product_name) and (i.quantity[j] > count):
                    useful_shops.append(i)
        if should_i_print is True:
            print(*useful_shops, sep='\n')
        return useful_shops

    def find_products(self, products):
        pass

    def sort_shops_by_product_price(self, product):
        price_lst = []
        shops_with_product = self.find_product(product, False) # ищет магазины, в которых есть этот продукт
        for i in shops_with_product:
            price_lst.append(i.prices[i.products.index(product)])
            # берётся индекс искомого продукта из класса магазина из списка продуктов, и с таким же
            # индексом цена этого продукта из списка цен
        for j in range(len(shops_with_product)):
            print(f'{shops_with_product[price_lst.index(min(price_lst))]}: {min(price_lst)} рублей')
            if len(price_lst) > 1:
                index_for_delete = price_lst.index(min(price_lst))
                price_lst.pop(index_for_delete)
                shops_with_product.pop(index_for_delete)

    def sort_shops_by_product_count(self, product):
        quantity_lst = []
        shops_with_product = self.find_product(product, False)  # ищет магазины, в которых есть этот продукт
        for i in shops_with_product:
            quantity_lst.append(i.quantity[i.products.index(product)])
            # берётся индекс искомого продукта из класса магазина из списка продуктов, и с таким же
            # индексом цена этого продукта из списка цен
        for j in range(len(shops_with_product)):
            print(f'{shops_with_product[quantity_lst.index(max(quantity_lst))]}: {max(quantity_lst)} штук')
            if len(quantity_lst) > 1:
                index_for_delete = quantity_lst.index(max(quantity_lst))
                quantity_lst.pop(index_for_delete)
                shops_with_product.pop(index_for_delete)


def buy(shop, product, count, user_name, save_check=False):
    shop.user_buy(product, count, user_name, save_check=save_check)


def save_changes(file_name):
    file = open(file_name + '.txt', 'w', encoding='utf-8')
    for shop in shops:
        products = ','.join(shop.products)
        file.write(';'.join([shop.name, products, str(shop.prices), str(shop.quantity)]) + '\n')
    file.close()


def load_data(file_name, rewrite=False):
    with open(file_name + '.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.split(';')
            name = line[0]
            products = line[1].split(',')
            prices = list(map(int, line[2][1:-1].split(', ')))
            quantity = list(map(int, line[3][1:-1].split(', ')))

            for shop in shops:
                if shop.name == name:
                    if rewrite:
                        shop.products = products
                        shop.prices = prices
                        shop.quantity = quantity
                    else:
                        shop.products.extend(products)
                        shop.prices.extend(prices)
                        shop.quantity.extend(quantity)


shops = [
    Shop(['моющее средство', 'мыло', 'маска', 'зубная паста', 'вода', 'шампунь', 'гель для душа'],
         [300, 100, 5000, 58, 7, 120, 300],
         [18, 50, 102, 33, 78, 4, 80],
         'Moydodyr'),
    Shop(["Война и Мир", "Зверобой", "Do what u r", "STFU", "Мандалорец", "Волкодав", "газеты", "маска"],
         [5000, 3100, 1999, 300, 100, 9999, 2700, 900],
         [4, 9, 2, 10, 2, 4, 8, 42],
         'Bigboyshop'),
    Shop(["сумка", "куртка", "маска", "шапка", "ремень", "кошель", "футболка", "STFU"],
         [10000, 23000, 9999, 10, 3467, 9123, 4823, 79999],
         [10, 2, 1, 3700, 12, 8, 1000],
         'Prada'),
    Shop(["croissant", "bread", "butter", "milk", "water", "newspapers", "yogurt", "mask", "soap", "t-shirt"],
         [34, 20, 400, 50, 20, 100, 49, 99, 1999, 1],
         [8, 12, 50, 17, 100, 288, 43, 35, 9, 102323],
         'Nezachetochka')
]

buy(shops[3], 'water', 2, 'Kirill', True)
# print(Nezachetochka().quantity[Nezachetochka().products.index('маска')])
save_changes('data')