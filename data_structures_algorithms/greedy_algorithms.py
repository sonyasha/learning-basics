from random import randint
from typing import List


class Item:
    def __init__(self, item_weight: int, item_value: int):
        self.weight = item_weight
        self.value = item_value
        self.value_per_weight = item_value / item_weight if item_weight != 0 else 0
        self.fraction = 1.0

    def __str__(self) -> str:
        return f"(weight: {self.weight}, value: {self.value}, value/weight: {self.value_per_weight}"

    def __repr__(self) -> str:
        return f"(weight: {self.weight}, value: {self.value}, value/weight: {self.value_per_weight}"


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


class FractionalKnapsack(Knapsack):
    def _fit_items(self) -> None:
        item_list = sorted(self.item_list, key=lambda x: x.value_per_weight, reverse=True)
        remaining_weight = self.max_weight
        for item in item_list:
            if item.weight <= remaining_weight:
                self.fitted_items.append(item)
                remaining_weight -= item.weight
            else:
                item.fraction = remaining_weight / item.weight
                self.fitted_items.append(item)
                break

        self.total_weight = sum([item.weight * item.fraction for item in self.fitted_items])
        self.total_value = sum([item.value * item.fraction for item in self.fitted_items])


def generate_items(num_items: int = 5) -> List[Item]:
    """Generate a specified number of random items."""
    items = []
    for _ in range(num_items):
        items.append(Item(randint(1, 30), randint(5, 20)))  # nosec
    return items


class Activity:
    def __init__(self, name, start_time, finish_time):
        self.name = name
        self.start_time = start_time
        self.finish_time = finish_time

    def __str__(self) -> str:
        return f"(name: {self.name}, start: {self.start_time}, finish: {self.finish_time}"

    def __repr__(self) -> str:
        return f"(name: {self.name}, start: {self.start_time}, finish: {self.finish_time}"


class Schedule:
    def __init__(self, activities: List[Activity]):
        self.activities = sorted(activities, key=lambda x: x.finish_time)
        self.confirmed_activities = []

    def _configure_schedule(self) -> None:
        current_finish_time = self.activities[0].finish_time
        self.confirmed_activities.append(self.activities[0])
        for activity in self.activities[1:]:
            if activity.start_time >= current_finish_time:
                self.confirmed_activities.append(activity)
                current_finish_time = activity.finish_time

    def get_confirmed_activities(self) -> List[Activity]:
        self._configure_schedule()
        return self.confirmed_activities


if __name__ == "__main__":
    # items = generate_items(5)
    # knapsack = Knapsack(50, items)
    # print(knapsack.get_stats())

    # fractional_knapsack = FractionalKnapsack(50, items)
    # print(fractional_knapsack.get_stats())

    # Activity scheduling
    activities = [
        Activity("A", 0, 3),
        Activity("B", 1, 4),
        Activity("C", 2, 5),
        Activity("D", 3, 6),
        Activity("E", 4, 7),
        Activity("F", 5, 8),
        Activity("G", 6, 9),
    ]
    schedule = Schedule(activities)
    print(schedule.get_confirmed_activities())
