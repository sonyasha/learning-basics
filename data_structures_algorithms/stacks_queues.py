# Array-based implementation of a stack and queue


class ArrayStack:
    # Initializes the stack. If the optional_max_length argument is omitted or
    # negative, the stack is unbounded. If optional_max_length is non-negative,
    # the stack is bounded.
    def __init__(self, optional_max_length=-1):
        self.stack_list = []
        self.max_length = optional_max_length

    #
    # Gets the length of the stack
    def __len__(self):
        return len(self.stack_list)

    #
    # Pops and returns the stack's top item.
    def pop(self):
        return self.stack_list.pop()

    #
    # Pushes an item, provided the push doesn't exceed bounds. Does nothing
    # otherwise. Returns True if the push occurred, False otherwise.
    def push(self, item):
        # If at max length, return false
        if len(self.stack_list) == self.max_length:
            return False
        #
        # If unbounded, or bounded and not yet at max length, then push
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
        # If at max length, return False
        if self.length == self.max_length:
            return False

        # Resize if length equals allocation size
        if self.length == len(self.queue_list):
            self.resize()

        # Enqueue the item
        item_index = (self.front_index + self.length) % len(self.queue_list)
        self.queue_list[item_index] = item
        self.length += 1
        return True

    # EXPERIMENTAL:
    # Implementation of enqueue that never requires a resize
    def enqueue_noresize(self, item):
        # If at max length, return False
        if self.length == self.max_length:
            return False

        if self.length < len(self.queue_list):
            # Space already exists in the list
            item_index = (self.front_index + self.length) % len(self.queue_list)
            self.queue_list[item_index] = item
        else:
            if self.front_index > 0:
                # Reorganize the list so that front_index is 0
                self.queue_list = self.queue_list[self.front_index :] + self.queue_list[0 : self.front_index]
                self.front_index = 0
            # Append the item
            self.queue_list.append(item)
        # All cases above enqueue the item, so length must be incremented
        self.length += 1
        return True

    def dequeue(self):
        # Get the item at the front of the queue
        to_return = self.queue_list[self.front_index]

        # Decrement length and advance frontIndex
        self.length -= 1
        self.front_index = (self.front_index + 1) % len(self.queue_list)

        # Return the front item
        return to_return

    def resize(self):
        # Create new list and copy existing items
        new_size = len(self.queue_list) * 2
        if self.max_length >= 0 and new_size > self.max_length:
            new_size = self.max_length
        new_list = [0] * new_size
        for i in range(self.length):
            item_index = (self.front_index + i) % len(self.queue_list)
            new_list[i] = self.queue_list[item_index]

        # Assign new list and reset front_index to 0
        self.queue_list = new_list
        self.front_index = 0


# Implementation of a queue using a linked list
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
            if succeeding_node is None:  # Removed last item
                self.tail = None
        elif current_node.next is not None:
            succeeding_node = current_node.next.next
            current_node.next = succeeding_node
            if succeeding_node is None:  # Removed tail
                self.tail = current_node


class Stack:
    def __init__(self):
        self.list = LinkedList()

    def push(self, new_item):
        # Create a new node to hold the item
        new_node = Node(new_item)

        # Insert the node as the list head (top of stack)
        self.list.prepend(new_node)

    def pop(self):
        # Copy data from list's head node (stack's top node)
        popped_item = self.list.head.data

        # Remove list head
        self.list.remove_after(None)

        # Return the popped item
        return popped_item


class Queue:
    def __init__(self):
        self.list = LinkedList()

    def enqueue(self, new_item):
        # Create a new node to hold the item
        new_node = Node(new_item)

        # Insert as list tail (end of queue)
        self.list.append(new_node)

    def dequeue(self):
        # Copy data from list's head node (queue's front node)
        dequeued_item = self.list.head.data

        # Remove list head
        self.list.remove_after(None)

        # Return the dequeued item
        return dequeued_item
