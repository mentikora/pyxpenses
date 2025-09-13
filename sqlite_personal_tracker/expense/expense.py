from dataclasses import dataclass

Category = {
    "transport",
    "food",
    "home",
    "delivery",
    "entertainment",
    "shopping",
    "health",
    "education",
    "other",
}


@dataclass
class Expense:
    amount: int | float
    category: str
    comment: str = None
    date: str = None

    def __post_init__(self) -> None:
        if self.category not in Category:
            raise ValueError("Invalid category: {}".format(self.category))
