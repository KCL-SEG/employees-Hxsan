"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class MonthlyEmployee():
    def __init__(self, name, salary, commissionBonus, rateAmount):
        self.name = name
        self.salary = salary
        self.commissionBonus = commissionBonus
        self.rateAmount = rateAmount
        self.statement = ""

    def pay(self):
        total = self.salary
        return total

    def get_pay(self):
        return self.pay()
    
    def Statement(self):
        if self.commissionBonus == 1:
            self.statement = f" and receives a bonus commission of {str(self.rateAmount)}"
        elif self.commissionBonus > 1:
            self.statement = f" and receives a commission for {str(self.commissionBonus)} contract(s) at {str(self.rateAmount)}/contract"

    def __str__(self):
        self.Statement()
        return f'{str(self.name)} works on a monthly salary of {str(self.salary)}{str(self.statement)}. Their total pay is {str(self.get_pay())}.'

class ContractEmployee():
    def __init__(self, name, hours, rate, commissionBonus, rateAmount):
        self.name = name
        self.hours = hours
        self.rate = rate
        self.commissionBonus = commissionBonus
        self.rateAmount = rateAmount
        self.statement = ""

    def pay(self):
        base = self.hours * self.rate
        bonus = self.commissionBonus * self.rateAmount

        total = base + bonus

        return total
    
    def get_pay(self):
        return self.pay()
    
    def Statement(self):
        if self.commissionBonus == 1:
            self.statement =  f' and receives a bonus commission of {str(self.rateAmount)}'
        elif self.commissionBonus > 1:
            self.statement =  f' and receives a commission for {str(self.commissionBonus)} contract(s) at {str(self.rateAmount)}/contract'
    
    def __str__(self):
        self.Statement()
        return f"{str(self.name)} works on a contract of {str(self.hours)} hours at {str(self.rate)}/hour{str(self.statement)}. Their total pay is {str(self.get_pay())}."


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = MonthlyEmployee('Billie', 4000, 0, 0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = ContractEmployee('Charlie', 100, 25, 0, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = MonthlyEmployee('Renee', 3000, 4, 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = ContractEmployee('Jan', 150, 25, 3, 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = MonthlyEmployee('Robbie', 2000, 1, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = ContractEmployee('Ariel', 120, 30, 1, 600)
