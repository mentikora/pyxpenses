from db import Database

from .expense import Expense
from .expenses import Expenses


class ExpensesRepository:
    """Responsible for creating expense, adding to collection and pushing
    to the database
    """

    def __init__(self, db: Database) -> None:
        self.expenses = Expenses()
        self.db = db

    def add(self, expense: Expense) -> None:
        query = (
            "INSERT INTO Expenses (amount, category, comment, date) VALUES (?, ?, ?, ?)"
        )
        query_params = (expense.amount, expense.category, expense.comment, expense.date)

        self.db.run(query=query, params=query_params)
        self.expenses.add(expense)

    def list(self) -> list[Expense]:
        return self.expenses.list()
