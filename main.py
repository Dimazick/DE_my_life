purchases = [
{"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
   {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3}]

#согласно букве S в принцыпах SOLID - делаю функции, которые только считают. Выводы делаю в Принтах.
def total_revenue(purchases):
    summa = 0
    for product in purchases:
        summa+= product['price'] * product['quantity']
    return summa
#Верните словарь, где ключ — категория, а значение — список уникальных товаров в этой категории.
def items_by_category(purchases):
    result = {}
    for product in purchases:
        cat = product["category"]
        item = product["item"]
        if cat not in result:
            result[cat] = []
        if item not in result[cat]:
            result[cat].append(item)
    return result

#Выведите все покупки, где цена товара больше или равна min_price
def expensive_purchases(purchases, min_price):
    result = []
    for product in purchases:
        if product["price"] > min_price:
            result.append(product)
    return result
#Рассчитайте среднюю цену товаров по каждой категории.
def average_price_by_category(purchases):
    result = {}
    counts = {}
    for product in purchases:
        cat = product["category"]
        price = product["price"]
        if cat not in result:
            result[cat] = 0
            counts[cat] = 0
        result[cat] += price
        counts[cat] += 1
    for cat in result:
        result[cat] /= counts[cat]
    return result
#Найдите и верните категорию, в которой куплено больше всего единиц товаров (учитывайте поле quantity).
def most_frequent_category(purchases):
    category_quantities = {}
    for product in purchases:
        category = product["category"]
        quantity = product["quantity"]

        if category not in category_quantities:
            category_quantities[category] = 0

        category_quantities[category] += quantity
        max_category = max(category_quantities, key=category_quantities.get)
    return max_category
print(f"Общая выручка: {total_revenue(purchases)}")
print(f"Товары по категориям: {items_by_category(purchases)}")
min_price = 1.0 #вводим цену, товары, дороже которой будем искать
print(f"Покупки дороже {min_price}: {expensive_purchases(purchases, min_price)}")
print(f"Средняя цена по категориям: {average_price_by_category(purchases)}")
print(f"Категория с наибольшим количеством проданных товаров: {most_frequent_category(purchases)}")