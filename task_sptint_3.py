# -*- coding: utf-8 -*-

import datetime


class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {
            "чипсы": 50,
            "кола": 100,
            "печенье": 45,
            "молоко": 55,
            "кефир": 70,
        }
        self.__tax_rate = {
            "чипсы": 20,
            "кола": 20,
            "печенье": 20,
            "молоко": 10,
            "кефир": 10,
        }

    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items

    def add_item_to_cheque(self, name):
        if not name or len(name) > 40:
            raise ValueError(
                "Нельзя добавить товар, если в его названии нет символов или их больше 40"
            )

        if name not in self.__item_price:
            raise NameError("Позиция отсутствует в товарном справочнике")

        self.__name_items.append(name)
        self.__number_items += 1

    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError("Позиция отсутствует в чеке")

        self.__name_items.remove(name)
        self.__number_items -= 1

    def check_amount(self):
        total = []
        for name in self.__name_items:
            total.append(self.__item_price[name])

        if len(self.__name_items) > 10:
            return sum(total) * 0.9
        else:
            return sum(total)

    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []
        for name in self.__name_items:
            if self.__tax_rate[name] == 20:
                twenty_percent_tax.append(name)

        for name in twenty_percent_tax:
            total.append(self.__item_price[name])

        subtotal = sum(total)

        if len(self.__name_items) > 10:
            subtotal *= 0.9

        nds = subtotal * 0.2
        return nds

    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []
        for name in self.__name_items:
            if self.__tax_rate[name] == 10:
                ten_percent_tax.append(name)

        for name in ten_percent_tax:
            total.append(self.__item_price[name])

        subtotal = sum(total)

        if len(self.__name_items) > 10:
            subtotal *= 0.9

        nds = subtotal * 0.1
        return nds

    def total_tax(self):
        return (
            self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation()
        )

    @staticmethod
    def get_telephone_number(telephone_number):
        phone_str = str(tephone_number)
        if not phone_str.isdigit():
            raise ValueError("Необходимо ввести цифры")

        if len(phone_str) != 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')

        return f"+7 {phone_str}"

    @staticmethod
    def get_date_and_time():
        now = datetime.datetime.now()
        date_and_time = []

        date = [
            ["часы", lambda x: x.hour],
            ["минуты", lambda x: x.minute],
            ["день", lambda x: x.day],
            ["месяц", lambda x: x.month],
            ["год", lambda x: x.year],
        ]

        for item in date:
            key = item[0]
            value = item[1](now)
            date_and_time.append(f"{key}: {value}")

        return date_and_time


if __name__ == "__main__":
    register = OnlineSalesRegisterCollector()

    # Добавляем товары
    register.add_item_to_cheque("чипсы")
    register.add_item_to_cheque("кола")
    register.add_item_to_cheque("молоко")
    register.add_item_to_cheque("молоко")
    register.add_item_to_cheque("молоко")
    register.add_item_to_cheque("молоко")
    register.add_item_to_cheque("молоко")
    register.add_item_to_cheque("молоко")
    register.add_item_to_cheque("молоко")
    register.add_item_to_cheque("молоко")

    print("Товары в чеке:", register.name_items)
    print("Количество товаров:", register.number_items)
    print("Общая сумма:", register.check_amount())
    print("Налог 20%:", register.twenty_percent_tax_calculation())
    print("Налог 10%:", register.ten_percent_tax_calculation())
    print("Итого налог:", register.total_tax())

    # Проверка телефона
    print("Телефон:", register.get_telephone_number("9876543210"))

    # Дата и время
    print("Дата и время:", register.get_date_and_time())
