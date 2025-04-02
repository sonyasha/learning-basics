from typing import List
from random import randint

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
        self.fitting_items = []


    def get_fitting_items(self):
        item_list = sorted(self.item_list, key = lambda x: x.value, reverse = True)
        remaining_weight = self.max_weight
        for item in item_list:
            if item.weight <= remaining_weight:
                self.fitting_items.append(item)
                remaining_weight -= item.weight

        total_weight = sum([item.weight for item in self.fitting_items])
        total_value = sum([item.value for item in self.fitting_items])
        return f"Total weight: {total_weight}, total value: {total_value}"


def get_items(number_of_items: int=5):
    items = []
    for i in range(number_of_items):
        items.append(Item(randint(1, 30), randint(5, 20)))
    return items

if __name__ == '__main__':
    knapsack = Knapsack(50, get_items(5))
    print(knapsack.item_list)
    print(knapsack.get_fitting_items())
    