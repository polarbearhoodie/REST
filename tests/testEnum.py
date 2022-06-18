from enum import Enum


class MaAsd(Enum):
    INCOME = "Income"
    EXPENSE = "Expense"


print(MaAsd.INCOME.name)
print("income")
