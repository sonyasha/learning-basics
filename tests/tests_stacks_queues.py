import unittest

from data_structures_algorithms.stacks_queues import ArrayQueue, ArrayStack, Queue, Stack


class TestArrayStack(unittest.TestCase):
    def test_init(self):
        # Test unbounded stack
        stack = ArrayStack()
        self.assertEqual(len(stack), 0)
        self.assertEqual(stack.max_length, -1)

        # Test bounded stack
        stack = ArrayStack(5)
        self.assertEqual(len(stack), 0)
        self.assertEqual(stack.max_length, 5)

    def test_push_pop(self):
        stack = ArrayStack()

        # Test push
        self.assertTrue(stack.push(10))
        self.assertEqual(len(stack), 1)

        self.assertTrue(stack.push(20))
        self.assertEqual(len(stack), 2)

        # Test pop
        self.assertEqual(stack.pop(), 20)
        self.assertEqual(len(stack), 1)

        self.assertEqual(stack.pop(), 10)
        self.assertEqual(len(stack), 0)

    def test_bounded_stack(self):
        stack = ArrayStack(2)

        # Fill the stack
        self.assertTrue(stack.push(10))
        self.assertTrue(stack.push(20))

        # Try to push when stack is full
        self.assertFalse(stack.push(30))
        self.assertEqual(len(stack), 2)

        # Pop and then push should work
        self.assertEqual(stack.pop(), 20)
        self.assertTrue(stack.push(30))

    def test_pop_empty(self):
        stack = ArrayStack()

        # Test pop on empty stack should raise IndexError
        with self.assertRaises(IndexError):
            stack.pop()


class TestArrayQueue(unittest.TestCase):
    def test_init(self):
        # Test unbounded queue
        queue = ArrayQueue()
        self.assertEqual(queue.get_length(), 0)
        self.assertEqual(queue.get_max_length(), -1)

        # Test bounded queue
        queue = ArrayQueue(5)
        self.assertEqual(queue.get_length(), 0)
        self.assertEqual(queue.get_max_length(), 5)

    def test_enqueue_dequeue(self):
        queue = ArrayQueue()

        # Test enqueue
        self.assertTrue(queue.enqueue(10))
        self.assertEqual(queue.get_length(), 1)

        self.assertTrue(queue.enqueue(20))
        self.assertEqual(queue.get_length(), 2)

        # Test dequeue
        self.assertEqual(queue.dequeue(), 10)
        self.assertEqual(queue.get_length(), 1)

        self.assertEqual(queue.dequeue(), 20)
        self.assertEqual(queue.get_length(), 0)

    def test_bounded_queue(self):
        queue = ArrayQueue(2)

        # Fill the queue
        self.assertTrue(queue.enqueue(10))
        self.assertTrue(queue.enqueue(20))

        # Try to enqueue when queue is full
        self.assertFalse(queue.enqueue(30))
        self.assertEqual(queue.get_length(), 2)

        # Dequeue and then enqueue should work
        self.assertEqual(queue.dequeue(), 10)
        self.assertTrue(queue.enqueue(30))

    def test_resize(self):
        queue = ArrayQueue()
        original_size = len(queue.queue_list)

        # Fill the queue to trigger resize
        for i in range(original_size + 1):
            queue.enqueue(i)

        # Check if resize happened
        self.assertTrue(len(queue.queue_list) > original_size)

        # Check if all elements are preserved
        for i in range(original_size + 1):
            self.assertEqual(queue.dequeue(), i)

    def test_enqueue_noresize(self):
        queue = ArrayQueue()

        # Add some items
        queue.enqueue_noresize(10)
        queue.enqueue_noresize(20)

        # Check front pointer behavior
        original_front = queue.front_index
        queue.dequeue()  # Should adjust front_index
        self.assertNotEqual(original_front, queue.front_index)

        # Test wrapping behavior by filling, then dequeuing, then filling again
        queue = ArrayQueue(4)
        for i in range(4):
            queue.enqueue_noresize(i)

        for _ in range(2):
            queue.dequeue()

        queue.enqueue_noresize(100)
        queue.enqueue_noresize(200)

        # Should get items in correct order
        expected = [2, 3, 100, 200]
        for expected_val in expected:
            self.assertEqual(queue.dequeue(), expected_val)


class TestLinkedListStack(unittest.TestCase):
    def test_push_pop(self):
        stack = Stack()

        # Push items
        stack.push(10)
        stack.push(20)
        stack.push(30)

        # Verify LIFO order when popping
        self.assertEqual(stack.pop(), 30)
        self.assertEqual(stack.pop(), 20)
        self.assertEqual(stack.pop(), 10)

    def test_pop_empty(self):
        stack = Stack()

        # Push and pop one item
        stack.push(10)
        self.assertEqual(stack.pop(), 10)

        # Test pop on empty stack should raise AttributeError
        # (since attempting to access head.data when head is None)
        with self.assertRaises(AttributeError):
            stack.pop()


class TestLinkedListQueue(unittest.TestCase):
    def test_enqueue_dequeue(self):
        queue = Queue()

        # Enqueue items
        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)

        # Verify FIFO order when dequeuing
        self.assertEqual(queue.dequeue(), 10)
        self.assertEqual(queue.dequeue(), 20)
        self.assertEqual(queue.dequeue(), 30)

    def test_dequeue_empty(self):
        queue = Queue()

        # Enqueue and dequeue one item
        queue.enqueue(10)
        self.assertEqual(queue.dequeue(), 10)

        # Test dequeue on empty queue should raise AttributeError
        # (since attempting to access head.data when head is None)
        with self.assertRaises(AttributeError):
            queue.dequeue()


if __name__ == "__main__":
    unittest.main()
