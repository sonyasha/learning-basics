from random import randint
from typing import List


class Item:
    def __init__(self, item_weight: int, item_value: int):
        self.weight = item_weight
        self.value = item_value

    def __str__(self) -> str:
        return f"(weight: {self.weight}, value: {self.value})"

    def __repr__(self) -> str:
        return f"(weight: {self.weight}, value: {self.value})"


class Knapsack:
    def __init__(self, max_weight: int, item_list: List[Item]):
        self.max_weight = max_weight
        self.item_list = item_list
        self.fitted_items = []
        self.total_weight = 0
        self.total_value = 0

    def _fit_items(self) -> None:
        item_list = sorted(self.item_list, key=lambda x: x.value, reverse=True)
        remaining_weight = self.max_weight
        for item in item_list:
            if item.weight <= remaining_weight:
                self.fitted_items.append(item)
                remaining_weight -= item.weight

        self.total_weight = sum([item.weight for item in self.fitted_items])
        self.total_value = sum([item.value for item in self.fitted_items])

    def get_stats(self) -> str:
        self._fit_items()
        output = (
            f"Max weight: {self.max_weight},\ntotal weight: {self.total_weight},\ntotal value: {self.total_value}\n"
        )
        return output + "Items:\n" + "\n".join([str(item) for item in self.fitted_items])


def generate_items(num_items: int = 5) -> List[Item]:
    """Generate a specified number of random items."""
    items = []
    for _ in range(num_items):
        items.append(Item(randint(1, 30), randint(5, 20)))
    return items


if __name__ == "__main__":
    knapsack = Knapsack(50, generate_items(5))
    print(knapsack.get_stats())
