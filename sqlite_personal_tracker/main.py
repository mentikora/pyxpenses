from expense.expenses_repository import ExpensesRepository
from expense.expense import Expense
from db import Database

db = Database('expenses.py')
repository = ExpensesRepository(db)

for x in range(10):
    repository.add(
        Expense(
            amount=x,
            category='home',
            comment=f'{x} expense comment'
        )
    )

rows = db.run(
    query='select * from Expenses',
    fetch=True
)

for row in rows:
    print(row)