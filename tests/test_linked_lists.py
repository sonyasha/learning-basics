import unittest

from data_structures_algorithms.linked_lists import DoublyLinkedList, DoublyNode, Node, SinglyLinkedList


class TestNode(unittest.TestCase):
    def test_node_creation(self):
        node = Node(10)
        self.assertEqual(node.data, 10)
        self.assertIsNone(node.next)


class TestDoublyNode(unittest.TestCase):
    def test_doubly_node_creation(self):
        node = DoublyNode(20)
        self.assertEqual(node.data, 20)
        self.assertIsNone(node.next)
        self.assertIsNone(node.prev)


class TestSinglyLinkedList(unittest.TestCase):
    def setUp(self):
        self.sll = SinglyLinkedList()

    def test_append_node(self):
        node1 = Node(10)
        node2 = Node(20)
        self.sll.append_node(node1)
        self.sll.append_node(node2)
        self.assertEqual(self.sll.head, node1)
        self.assertEqual(self.sll.tail, node2)
        self.assertEqual(self.sll.head.next, node2)

    def test_prepend_node(self):
        node1 = Node(10)
        node2 = Node(20)
        self.sll.prepend_node(node1)
        self.sll.prepend_node(node2)
        self.assertEqual(self.sll.head, node2)
        self.assertEqual(self.sll.tail, node1)
        self.assertEqual(self.sll.head.next, node1)

    def test_insert_after(self):
        node1 = Node(10)
        node2 = Node(20)
        node3 = Node(15)
        self.sll.append_node(node1)
        self.sll.append_node(node2)
        self.sll.insert_after(node1, node3)
        self.assertEqual(node1.next, node3)
        self.assertEqual(node3.next, node2)

    def test_remove_after(self):
        node1 = Node(10)
        node2 = Node(20)
        self.sll.append_node(node1)
        self.sll.append_node(node2)
        self.sll.remove_after(node1)
        self.assertIsNone(node1.next)
        self.assertEqual(self.sll.tail, node1)

    def test_get_node(self):
        node1 = Node(10)
        node2 = Node(20)
        self.sll.append_node(node1)
        self.sll.append_node(node2)
        found_node = self.sll.get_node(20)
        self.assertEqual(found_node, node2)

    def test_insert_sort(self):
        node1 = Node(30)
        node2 = Node(10)
        node3 = Node(20)
        self.sll.append_node(node1)
        self.sll.append_node(node2)
        self.sll.append_node(node3)
        self.sll.insert_sort()
        self.assertEqual(self.sll.head.data, 10)
        self.assertEqual(self.sll.head.next.data, 20)
        self.assertEqual(self.sll.tail.data, 30)


class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.dll = DoublyLinkedList()

    def test_append_node(self):
        node1 = DoublyNode(10)
        node2 = DoublyNode(20)
        self.dll.append_node(node1)
        self.dll.append_node(node2)
        self.assertEqual(self.dll.head, node1)
        self.assertEqual(self.dll.tail, node2)
        self.assertEqual(self.dll.head.next, node2)
        self.assertEqual(node2.prev, node1)

    def test_prepend_node(self):
        node1 = DoublyNode(10)
        node2 = DoublyNode(20)
        self.dll.prepend_node(node1)
        self.dll.prepend_node(node2)
        self.assertEqual(self.dll.head, node2)
        self.assertEqual(self.dll.tail, node1)
        self.assertEqual(self.dll.head.next, node1)
        self.assertEqual(node1.prev, node2)

    def test_insert_after(self):
        node1 = DoublyNode(10)
        node2 = DoublyNode(20)
        node3 = DoublyNode(15)
        self.dll.append_node(node1)
        self.dll.append_node(node2)
        self.dll.insert_after(node1, node3)
        self.assertEqual(node1.next, node3)
        self.assertEqual(node3.prev, node1)
        self.assertEqual(node3.next, node2)
        self.assertEqual(node2.prev, node3)

    def test_remove(self):
        node1 = DoublyNode(10)
        node2 = DoublyNode(20)
        self.dll.append_node(node1)
        self.dll.append_node(node2)
        self.dll.remove(node2)
        self.assertEqual(self.dll.tail, node1)
        self.assertIsNone(node1.next)

    def test_insert_sort(self):
        node1 = DoublyNode(30)
        node2 = DoublyNode(10)
        node3 = DoublyNode(20)
        self.dll.append_node(node1)
        self.dll.append_node(node2)
        self.dll.append_node(node3)
        self.dll.insert_sort()
        self.assertEqual(self.dll.head.data, 10)
        self.assertEqual(self.dll.head.next.data, 20)
        self.assertEqual(self.dll.tail.data, 30)


if __name__ == "__main__":
    unittest.main()
