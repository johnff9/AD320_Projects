class DLNode:
    def __init__(self, previous_node=None, data_portion=None, next_node=None):
        self.previous_node = previous_node
        self.data = data_portion
        self.next_node = next_node

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_previous_node(self):
        return self.previous_node

    def set_previous_node(self, previous_node):
        self.previous_node = previous_node


class LinkedDeque:
    def __init__(self):
        self.front = None  # First node
        self.back = None   # Last node
        self.size = 0      # Track the number of elements

    def add_to_back(self, new_entry):
        new_node = DLNode(previous_node=self.back, data_portion=new_entry)
        if self.is_empty():
            self.front = new_node
        else:
            self.back.set_next_node(new_node)
        self.back = new_node
        self.size += 1

    def add_to_front(self, new_entry):
        new_node = DLNode(next_node=self.front, data_portion=new_entry)
        if self.is_empty():
            self.back = new_node
        else:
            self.front.set_previous_node(new_node)
        self.front = new_node
        self.size += 1

    def get_back(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.back.get_data()

    def get_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.front.get_data()

    def remove_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        removed_data = self.front.get_data()
        self.front = self.front.get_next_node()
        if self.front is None:  # If list is now empty
            self.back = None
        else:
            self.front.set_previous_node(None)
        self.size -= 1
        return removed_data

    def remove_back(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        removed_data = self.back.get_data()
        self.back = self.back.get_previous_node()
        if self.back is None:  # If list is now empty
            self.front = None
        else:
            self.back.set_next_node(None)
        self.size -= 1
        return removed_data

    def clear(self):
        self.front = None
        self.back = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def display(self):
        current_node = self.front
        elements = []
        while current_node:
            elements.append(current_node.get_data())
            current_node = current_node.get_next_node()
        print("Deque:", elements)
