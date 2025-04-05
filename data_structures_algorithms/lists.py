from abc import ABC, abstractmethod


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class DoublyNode(Node):
    def __init__(self, data):
        super().__init__(data)
        self.prev = None


class LinkedList(ABC):
    def __init__(self):
        self.head = None
        self.tail = None

    @abstractmethod
    def append_node(self, node: Node) -> None:
        raise NotImplementedError

    @abstractmethod
    def prepend_node(self, node: Node) -> None:
        raise NotImplementedError

    @abstractmethod
    def insert_after(self, prev_node: Node, node: Node):
        raise NotImplementedError


class SinglyLinkedList(LinkedList):
    def append_node(self, node: Node) -> None:
        if not self.head:
            self.head = node
            self.tail = node
        else:
            old_tail = self.tail
            old_tail.next = node
            self.tail = node

    def prepend_node(self, node: Node) -> None:
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def insert_after(self, prev_node: Node, node: Node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = prev_node.next
            prev_node.next = node
            if self.tail == prev_node:
                self.tail = node

    def remove_after(self, prev_node: Node = None):
        if not self.head:
            pass
        # Remove head
        if not prev_node:
            prev_head = self.head
            successor_node = prev_head.next
            self.head = successor_node
            prev_head.next = None
            if not successor_node:
                self.tail = None
        else:
            node_to_delete = prev_node.next
            if node_to_delete:
                successor_node = node_to_delete.next
                prev_node.next = successor_node
                node_to_delete.next = None
                if not successor_node:
                    self.tail = prev_node

    def get_node(self, node_data) -> Node:
        current_node = self.head
        while current_node:
            if current_node.data == node_data:
                return current_node
            current_node = current_node.next
        return None

    def find_insert_position(self, data):
        current_node1 = None
        current_node2 = self.head
        while current_node2 and data > current_node2.data:
            current_node1 = current_node2
            current_node2 = current_node2.next
        return current_node1

    def insert_sort(self):
        prev_node = self.head
        current_node = self.head.next
        while current_node:
            next_node = current_node.next
            position = self.find_insert_position(current_node.data)

            if position == prev_node:
                prev_node = current_node.next
            else:
                self.remove_after(prev_node)
                if not position:
                    self.prepend_node(current_node)
                else:
                    self.insert_after(position, current_node)
            current_node = next_node

    def search_recursive(self, data, node: Node = None):
        start_node = node if node else self.header
        if start_node.data == data:
            return start_node
        self.search_recursive(data, start_node.next)
        return None


class DoublyLinkedList(LinkedList):
    def __init__(self):
        super().__init__()

    def append_node(self, node: Node) -> None:
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def prepend_node(self, node: Node) -> None:
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def insert_after(self, prev_node: Node, node: Node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            successor_node = prev_node.next
            node.next = successor_node
            node.prev = prev_node
            prev_node.next = node
            if successor_node:
                successor_node.prev = node
            if self.tail == prev_node:
                self.tail = node

    def remove(self, node: Node):
        if not self.head:
            pass
        predecessor_node = node.prev
        successor_node = node.next
        if predecessor_node:
            predecessor_node.next = successor_node
        if successor_node:
            successor_node.prev = predecessor_node
        if not predecessor_node:
            self.head = successor_node
        if not successor_node:
            self.tail = predecessor_node

    def insert_sort(self):
        """ "Insertion sort's typical runtime is O(N^2).
        If a list has N elements, the outer loop executes N - 1 times.
        For each outer loop execution, the inner loop may need to examine all elements in the sorted part.
        Thus, the inner loop executes on average N/2 times.
        So the total number of comparisons is proportional to (N-1) * (N/2) = O(N^2).
        In the best case scenario, the list is already sorted, and the runtime complexity is O(N).
        """
        current_node = self.head.next
        while current_node:
            if not self.head or not self.head.next:
                return
            search_node = current_node.prev
            next_node = current_node.next
            while search_node and search_node.data > current_node.data:
                search_node = search_node.prev
            self.remove(current_node)
            # Insert at the beginning if search_node is None
            if search_node is None:
                self.prepend_node(current_node)
            else:
                self.insert_after(search_node, current_node)

            current_node = next_node


class ArrayList:
    def __init__(self, capacity=10):
        self.array = [None] * capacity
        self.allocation_size = capacity
        self.length = 0

    def append(self, new_item):
        if self.allocation_size == self.length:
            self.resize(self.length * 2)

        self.array[self.length] = new_item
        self.length = self.length + 1

    def resize(self, new_allocation_size):
        new_array = [None] * new_allocation_size
        for i in range(self.length):
            new_array[i] = self.array[i]
        self.array = new_array

        # Update the allocation size
        self.allocation_size = new_allocation_size

    def prepend(self, new_item):
        if self.allocation_size == self.length:
            self.resize(self.length * 2)
        # Shift all array items to the right,
        # starting from the last index and moving
        # down to the first index.
        for i in reversed(range(1, self.length + 1)):
            self.array[i] = self.array[i - 1]
        self.array[0] = new_item
        self.length = self.length + 1

    def insert_after(self, index, new_item):
        if self.allocation_size == self.length:
            self.resize(self.length * 2)
        # Shift all the array items to the right,
        # starting from the last item and moving down to
        # the item just past the given index.
        for i in reversed(range(index + 1, self.length + 1)):
            self.array[i] = self.array[i - 1]
        self.array[index + 1] = new_item
        self.length = self.length + 1

    def search(self, item):
        for i in range(self.length):
            if self.array[i] == item:
                return i
        return -1

    def remove_at(self, index):
        if index >= 0 and index < self.length:
            for i in range(index, self.length - 1):
                self.array[i] = self.array[i + 1]
            self.length = self.length - 1
