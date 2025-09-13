class Wallet:
    """
    Represents Player's money
    """

    def __init__(self, initial_amount: int = 0):
        if initial_amount < 0:
            raise ValueError("Initial money cannot be negative")
        self._balance: int = initial_amount

    def deposit(self, amount: int):
        if amount < 0:
            raise ValueError("Cannot deposit negative amount")
        self._balance += amount

    def withdraw(self, amount: int):
        if amount < 0:
            raise ValueError("Cannot withdraw negative amount")
        if amount > self._balance:
            raise ValueError("Not enough money")
        self._balance -= amount

    @property
    def balance(self) -> int:
        return self._balance
