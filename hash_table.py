
class HashTable:

    def __init__(self, size=7):
        self.data_map = [None]*size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is None:
            return None
        else:
            for i in self.data_map[index]:
                if i[0] == key:
                    return i[1]

    def keys(self):
        keys = []
        for i in self.data_map:
            if i is not None:
                for j in i:
                    keys.append(j[0])
        return keys

    def delete_key(self, key):
        flag = 0
        index = self.__hash(key)
        for i in self.data_map[index]:
            if i[0] == key:
                flag = 1
                self.data_map[index].remove(i)
        if flag == 0:
            return None


h1 = HashTable()
h1.set_item("bolts", 12)
h1.set_item("nails", 20)
h1.set_item("hammer", 5)
h1.set_item("saw", 10)
h1.set_item("pipe", 8)
h1.print_table()
print(h1.get_item("saw"))
print(h1.keys())
print(h1.delete_key('scissor'))
h1.print_table()

