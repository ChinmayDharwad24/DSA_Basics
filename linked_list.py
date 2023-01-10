class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.tail = None
            self.head = None
        else:
            # temp = self.head
            # while temp == self.tail:
            #     temp = temp.next
            # self.tail = temp
            # self.tail.next = None
            # self.length -= 1
            temp = self.head
            prev = self.head
            while temp.next:
                prev = temp
                temp = temp.next
            self.tail = prev
            self.tail.next = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.head
            self.head = new_node
            self.head.next = temp
        self.length += 1
        return True

    def pop_first(self):
        temp = self.head
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        temp = self.head
        if index < 0 or index >= self.length:
            return None
        else:
            for i in range(0, index):
                temp = temp.next
            return temp

    def set(self, value, index):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, value, index):
        if index < 0 or index > self.length-1:
            return None
        elif index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            new_node = Node(value)
            prev = self.get(index-1)
            temp = self.get(index)
            prev.next = new_node
            new_node.next = temp
            return True

    def remove(self, index):
        if index < 0 or index > self.length-1:
            return None
        elif index == 0:
            self.pop_first()
        elif index == self.length:
            self.pop()
        else:
            prev = self.get(index - 1)
            temp = self.get(index)
            prev.next = temp.next
            temp.next = None
            return temp


ll1 = LinkedList(4)
ll1.prepend(5)
ll1.append(6)

ll1.insert(7, 2)
ll1.insert(3, 2)
ll1.print_list()
print("---------------")
ll1.remove(2)
ll1.print_list()
print("---------------")
ll1.set(3, 1)
ll1.print_list()
# print(ll1.get())
# print(ll1.pop())
# ll1.print_list()