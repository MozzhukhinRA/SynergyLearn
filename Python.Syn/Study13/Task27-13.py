class CashReg(object):

    def __init__(self, cash):
        self.cash = cash

    def top_up(self):
        plus = int(input("Введите сумму на которую хотите пополнить: "))
        self.cash += plus
        print(f'Сумма пополнена на: {plus}$. Сейчас в кассе: {self.cash}$')

    def count_1000(self):
        if self.cash >= 1000:
            ctn = self.cash // 1000
            print(f'{ctn}')
        else:
            print("Целых тысяч нет")

    def take_away(self):
        minus = int(input("Сколько забрать из кассы: "))
        if minus <= self.cash:
            self.cash -= minus
            print(f'Сейчас в кассе: {self.cash}$')
        else:
            print("Hе достаточно денег")

while True:
    n = input("Введите функцию - top_up, count_1000, take_away, exit: ")
    if n == 'top_up':
        h1 = CashReg(int(input("Сейчас в кассе: ")))
        h1.top_up()
    elif n == 'count_1000':
        h1 = CashReg(int(input("Сейчас в кассе: ")))
        h1.count_1000()
    elif n == 'take_away':
        h1 = CashReg(int(input("Сейчас в кассе: ")))
        h1.take_away()
    elif n == 'exit':
        break
    else:
        print("404 Not Found")

#Создайте класс Касса, который хранит текущее количество денег в кассе