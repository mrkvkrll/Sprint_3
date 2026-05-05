import datetime


class OnlineSalesRegisterCollector:


    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}


    @property
    def get_name_items(self):
        return self.__name_items  
    

    @property
    def get_number_items(self):
        return self.__number_items 
    

#Добавить товар в чек
    def add_item_to_cheque(self,name): 
        self.name = name
        if len(self.name) == 0 or len(self.name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40') 
        elif self.name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике') 
        else:
            self.__name_items.append(name)
            self.__number_items +=1
    

#Удалить товар из чека
    def delete_item_from_check(self, name):  
        self.name = name
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        else:
            self.__name_items.remove(name)
            self.__number_items -=1
    

#Посчитать общую стоимость товаров
    def check_amount(self):  
        total = 0
        for item in self.__name_items:
            if item in self.__item_price:
                total += self.__item_price[item]
        if self.__number_items > 10:
            total *= 0.9  
        return total
    

# рассчет НДС товаров, у которых налоговая ставка 10%. 
    def ten_percent_tax_calculation(self): 
        return self.nds_calculate(10)


# рассчет НДС товаров, у которых налоговая ставка 20%.
    def twenty_percent_tax_calculation(self):
        return self.nds_calculate(20)


    # def nds_calculate(self, nds):
    #     total_price = 0 
    #     for item in self.__name_items:
    #         if item in self.__item_price and self.__tax_rate[item] == nds:
    #             total_price += self.__item_price[item]
    #     if self.__number_items > 10:
    #         total_price *= 0.9   
    #     total = total_price * nds / 100
    #     return total
    
 #реализация по ТЗ со списком nds_percent_tax  
    def nds_calculate(self, nds):
        nds_percent_tax = []
        total_price = 0   
        for item in self.__name_items:
            if item in self.__item_price and self.__tax_rate[item] == nds:
                nds_percent_tax.append(item)
                total_price += self.__item_price[item]   
        if self.__number_items > 10:
            total_price *= 0.9   
        total = total_price * nds / 100
        return total


    def total_tax(self):  #Посчитать общую сумму налогов
        total = self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation()
        return total
    
#Вернуть номер телефона покупателя
    @staticmethod
    def get_telephone_number(telephone_number):
        telephone_number = str(telephone_number)
        if not telephone_number.isdigit():
            raise ValueError('Необходимо ввести цифры')
        elif len(telephone_number) != 10:
            raise  ValueError('Необходимо ввести 10 цифр после "+7"')
        else:
            return telephone_number
        
#Вернуть дату и время покупки
    @staticmethod
    def get_date_and_time():
        date_and_time = []
        now = datetime.datetime.now()
        date = [
                ['часы', (lambda x: x.hour) (now)],
                ['минуты', (lambda x: x.minute) (now)],
                ['день', (lambda x: x.day) (now)],
                ['месяц', (lambda x: x.month) (now)],
                ['год', (lambda x: x.year) (now)]
                 ]
        for item in date:
            date_and_time.append(f'{item[0]}: {item[1]}')
        return date_and_time


# register = OnlineSalesRegisterCollector()
# total = register.check_amount()
# print(f'Общая стоимость товаров: {total}')
# total = register.ten_percent_tax_calculation()
# print(f'НДС товаров, у которых налоговая ставка 10%, составляет: {total}')
# total = register.twenty_percent_tax_calculation()
# print(f'НДС товаров, у которых налоговая ставка 20%, составляет: {total}')
# total = register.total_tax()
# print(f'Общая сумма налогов составляет: {total}')
# telephone_number = register.get_telephone_number(1234697621)
# # telephone_number = register.get_telephone_number(123469621)
# # telephone_number = register.get_telephone_number("test_phone")
# print(f'Номер телефона покупателя: +7{telephone_number}')
# date_and_time = register.get_date_and_time()
# print(f'Дата и время покупки: {date_and_time}')
