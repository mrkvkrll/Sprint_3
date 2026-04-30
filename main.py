item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
name_items = ['кола','печенье','чипсы']
number_items = 3

def check_amount(): #Посчитать общую стоимость товаров 
    total = 0
    for i in range(len(name_items)):
        item = name_items[i]
        if item in item_price:
            total += item_price[item]
    if number_items > 2:
        total *=0.9    
    return total
print(check_amount())
    # if len(number_items) > 10:
    #     total.append(values * 0,9)
    # else:
    #     total.append(item_price.price)
    