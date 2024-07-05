'''
from account import Account
account = Account(123, "Henrique", 55.5)
account2 = Account(321, "Nico", 100)
'''
class Account:
    
    def __init__(self, number, holder, balance, limit=1000.0):
        self.__number   = number
        self.__holder   = holder
        self.__balance  = balance
        self.__limit    = limit
        
    def statement(self):
        print(f'{self.__holder} - Bank statement: {self.__balance}')
    
    def __check_withdraw(self, value):
        available_value = (self.__balance + self.__limit)
        return value <= available_value
    
    
    def withdraw(self, value):
        if self.__check_withdraw(value):
            self.__balance -= value
        else:
            print(f'The value [{value}] exceeded the limit [{self.__limit}]!')
        
    def deposit(self, value):
        self.__balance += value
        
    def transfer(self, value, receiver):
        self.withdraw(value)
        receiver.deposit(value)
        
    def get_holder(self):
        return self.__holder

    def get_balance(self):
        return self.__balance

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, limit):
        self.__limit = limit
        
    @staticmethod
    def bank_code():
        return '001'
    
    @staticmethod
    def banks_code():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}
        
            