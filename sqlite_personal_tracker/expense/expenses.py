from .expense import Expense


class Expenses:
    def __init__(self, expenses: list[Expense] = None) -> None:
        self.expenses = expenses or []

    def add(self, expense: Expense) -> None:
        self.expenses.append(expense)

    def list(self) -> list[Expense]:
        return self.expenses
