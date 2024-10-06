class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class SingleyLinkedLlist:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self._length = 0

    def append(self, value):
        # Time - 0(1)
        # Space - 0(1)
        new_node = Node(value)
        if not self._length:
            self.head = self.tail = None
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._length += 1
        return self
    
    def prepend(self, value):
        # Time - 0(1)
        # Space - 0(1)
        new_node = Node(value)
        if not self._length:
            self.head = self.tail = None
        else:
            new_node.next = self.head
            self.head = new_node
        self._length += 1
        return self

    def pop_left(self):
        # Time - 0(1)
        # Space - 0(1)
        if not self._length:
            raise Exception("List is empty!")
        former_head = self.head
        self.head = former_head.next
        former_head.next = None
        self._length -= 1
        if not self._length:
            self.tail = None
        return former_head.value
    
    def pop_right(self):
        # Time - 0(n)
        # Space - 0(1)
        if not self._length:
            raise Exception("List is empty!")
        tail_value = self.tail.value
        if self._length == 1:
            self.head = self.tail = None
        else:
            temp_node = self.head
            while temp_node.next is not self.tail:
                temp_node = temp_node.next
            self.tail = temp_node
            self.tail.next = None
        self._length -= 1
        return tail_value
    
    

