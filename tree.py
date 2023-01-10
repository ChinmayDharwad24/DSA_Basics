class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                elif new_node.value == temp.value:
                    return False
                else:
                    temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                elif new_node.value == temp.value:
                    return False
                else:
                    temp = temp.right

    def contains(self, value):
        temp = self.root
        if self.root is None:
            return False
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def min_val(self, current_node):
        temp = current_node
        while temp.left is not None:
            temp = temp.left
        return temp.value


t1 = BinarySearchTree()
t1.insert(17)
t1.insert(15)
t1.insert(25)
print(t1.root.left.value)
print(t1.root.right.value)
print("__________")
print(t1.contains(15))
print("-----------")
print(t1.contains(32))
print("----------")
print(t1.min_val(t1.root))



