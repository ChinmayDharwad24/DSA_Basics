class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.length = 1

    def push(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            self.is_empty()
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp

    def is_empty(self):
        if self.length == 0:
            return True

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def size(self):
        return self.length

    def peek(self):
        return self.top


s1 = Stack(2)
s1.push(3)
s1.print_stack()
print("___________")
# s1.print_stack()
print(s1.size())
print("--------------")
s1.push(4)
s1.push(5)
s1.print_stack()
print("-----------")
print(s1.peek().value)