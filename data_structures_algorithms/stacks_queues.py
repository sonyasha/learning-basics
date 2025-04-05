# Array-based implementation of a stack and queue
class ArrayStack:
    # Initializes the stack. If the optional_max_length argument is omitted or
    # negative, the stack is unbounded. If optional_max_length is non-negative,
    # the stack is bounded.
    def __init__(self, optional_max_length=-1):
        self.stack_list = []
        self.max_length = optional_max_length

    def __len__(self):
        return len(self.stack_list)

    def pop(self):
        return self.stack_list.pop()

    def push(self, item):
        if len(self.stack_list) == self.max_length:
            return False
        self.stack_list.append(item)
        return True


class ArrayQueue:
    def __init__(self, maximum_length=-1):
        self.queue_list = [0]
        self.front_index = 0
        self.length = 0
        self.max_length = maximum_length

    def get_length(self):
        return self.length

    def get_max_length(self):
        return self.max_length

    def enqueue(self, item):
        if self.length == self.max_length:
            return False

        if self.length == len(self.queue_list):
            self.resize()

        item_index = (self.front_index + self.length) % len(self.queue_list)
        self.queue_list[item_index] = item
        self.length += 1
        return True

    # Implementation of enqueue that never requires a resize
    def enqueue_noresize(self, item):
        if self.length == self.max_length:
            return False

        if self.length < len(self.queue_list):
            item_index = (self.front_index + self.length) % len(self.queue_list)
            self.queue_list[item_index] = item
        else:
            if self.front_index > 0:
                self.queue_list = self.queue_list[self.front_index :] + self.queue_list[0 : self.front_index]
                self.front_index = 0
            self.queue_list.append(item)
        self.length += 1
        return True

    def dequeue(self):
        to_return = self.queue_list[self.front_index]

        self.length -= 1
        self.front_index = (self.front_index + 1) % len(self.queue_list)

        return to_return

    def resize(self):
        new_size = len(self.queue_list) * 2
        if self.max_length >= 0 and new_size > self.max_length:
            new_size = self.max_length
        new_list = [0] * new_size
        for i in range(self.length):
            item_index = (self.front_index + i) % len(self.queue_list)
            new_list[i] = self.queue_list[item_index]

        self.queue_list = new_list
        self.front_index = 0


# Linked list implementation of a stack and queue
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_after(self, current_node, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif current_node is self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            new_node.next = current_node.next
            current_node.next = new_node

    def remove_after(self, current_node):
        # Special case, remove head
        if (current_node is None) and (self.head is not None):
            succeeding_node = self.head.next
            self.head = succeeding_node
            if succeeding_node is None:
                self.tail = None
        elif current_node.next is not None:
            succeeding_node = current_node.next.next
            current_node.next = succeeding_node
            if succeeding_node is None:
                self.tail = current_node


class Stack:
    def __init__(self):
        self.list = LinkedList()

    def push(self, new_item):
        new_node = Node(new_item)

        self.list.prepend(new_node)

    def pop(self):
        popped_item = self.list.head.data
        self.list.remove_after(None)
        return popped_item


class Queue:
    def __init__(self):
        self.list = LinkedList()

    def enqueue(self, new_item):
        new_node = Node(new_item)
        self.list.append(new_node)

    def dequeue(self):
        dequeued_item = self.list.head.data
        self.list.remove_after(None)
        return dequeued_item
