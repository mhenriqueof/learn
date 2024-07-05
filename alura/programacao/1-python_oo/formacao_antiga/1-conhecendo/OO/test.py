

def create_account(number, holder, balance, limit):
    account = {"Number": number, "Holder": holder, "Balance": balance, "Limit": limit}
    return account


def deposit(account, value):
    account["Balance"] += value
    

def withdraw(account, value):
    account["Balance"] -= value
    

def statement(account):
    print(f'Bank statement: {account["Balance"]}')
    