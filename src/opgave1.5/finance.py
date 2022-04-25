class Grouping:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0

    def __repr__(self):
        string = self.name.center(30, "*")
        for dic in self.ledger:
            for key, value in dic.items():
                stri = f"\n{key[:23]:<23}{value:>7}"
                string += stri
        total = f"\n{'totaal':<23}{self.balance:>7}"
        string += total
        return string

    def deposit(self, amount, description=""):
        amount = float(amount)
        self.balance += amount
        dictionary = {description: amount}
        self.ledger.append(dictionary)

    def withdraw(self, amount, description=""):
        amount = float(amount)
        if self.balance < amount:
            return False
        elif self.balance > amount:
            self.balance -= amount
            dictionary = {description: 0 - amount}
            self.ledger.append(dictionary)
            return True

    def get_balance(self):
        return self.balance

    def transfer(self, amount, group):
        amount = float(amount)
        group.withdraw(amount, "transfer")
        self.deposit((0 - amount), f"Transfer to {group.name}")

    def check_funds(self, amount):
        amount = float(amount)
        if self.balance < amount:
            return False
        else:
            return True


def create_spend_chart(groups):
    pass
