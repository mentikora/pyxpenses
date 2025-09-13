from db import Database
from expense.expense import Expense
from expense.expenses_repository import ExpensesRepository

db = Database("expenses.db")
repository = ExpensesRepository(db)

for x in range(10):
    repository.add(Expense(amount=x, category="home", comment=f"{x} expense comment"))

rows = db.run(query="select * from Expenses", fetch=True)

for row in rows:
    print(row)
