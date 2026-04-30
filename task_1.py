import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = ['кола','молоко','печенье','кефир']
        self.__number_items = 4
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def get_name_items(self):
        return self.__name_items  
    

    @property
    def get__number_items(self):
        return self.__number_items 
    

    def add_item_to_cheque(self,name):
        self.name = name
        if len(self.name) == 0 or len(self.name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40') 
        elif self.name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике') 
        else:
            self.__name_items.append(name)
            self.__number_items +=1
        return f'{self.__name_items },{self.__item_price}, {self.__number_items}' 
    

    def delete_item_from_check(self, name):
        self.name = name
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        else:
            self.__name_items.remove(name)
            self.__number_items -=1
        return f'{self.__name_items }, {self.__item_price}, {self.__number_items}' 
    

    def check_amount(self): #Посчитать общую стоимость товаров 
        total = 0
        for i in range(self.__number_items):
            item = self.__name_items[i]
            if item in self.__item_price:
                total += self.__item_price[item]
        if self.__number_items > 10:
            total *= 0.9    
        return total
    

    def twenty_percent_tax_calculation(self): # рассчет НДС товаров, у которых налоговая ставка 20%.
        twenty_percent_tax = []
        total = 0
        for i in range(len(self.__name_items)):
            item = self.__name_items[i]
            if item in self.__item_price and self.__tax_rate[item] == 20:
                twenty_percent_tax.append(self.__name_items[i])
                total += self.__item_price[item]
            if self.__number_items > 10:
                total *= 0.9
        return total * 0.2


    def ten_percent_tax_calculation(self): # рассчет НДС товаров, у которых налоговая ставка 10%.
        twenty_percent_tax = []
        total = 0
        for i in range(len(self.__name_items)):
            item = self.__name_items[i]
            if item in self.__item_price and self.__tax_rate[item] == 10:
                twenty_percent_tax.append(self.__name_items[i])
                total += self.__item_price[item]
            if self.__number_items > 10:
                total *= 0.9
        return total * 0.1

    def total_tax(self):
        return self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation()
    

    @staticmethod
    def get_telephone_number(telephone_number):
        telephone_number = str(telephone_number)
        if not telephone_number.isdigit():
            raise ValueError('Необходимо ввести цифры')
        elif len(telephone_number) != 10:
            raise  ValueError('Необходимо ввести 10 цифр после "+7"')
        else:
            return f'+7{telephone_number}'
        


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




    



register = OnlineSalesRegisterCollector()
print(register.add_item_to_cheque('чипсы'))
print(register.delete_item_from_check('молоко'))
print(register.twenty_percent_tax_calculation())
print(register.ten_percent_tax_calculation())
print(register.total_tax())
print(register.get_date_and_time())

