# key value pair storage
#to solve hash collision- 1. Linear probing
#                         2. Chaining

class hash:
    def __init__(self):
        self.MAX=20
        self.arr = [ None for i in range(self.MAX)]

    def get_hashkey(self,key):
        hash=0
        for char in key:
            hash+=ord(char)
        return hash %  self.MAX

    def __getitem__(self, item):
        h= self.get_hashkey(index)
        return self.arr[h]

    def __setitem__(self, key, value):
        h=self.get_hashkey(key)
        self.arr[h]=value


    def __delitem__(self, key):
        h= self.get_hashkey(key)
        self.arr[h] = None

    def print_hash_table(self):
        for i in range(self.MAX):
            print(self.arr[i],end=" ")


class HashTable_with_chainning:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __getitem__(self, key):
        arr_index = self.get_hash(key)
        for kv in self.arr[arr_index]:
            if kv[0] == key:
                return kv[1]

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
        if not found:
            self.arr[h].append((key, val))

    def __delitem__(self, key):
        arr_index = self.get_hash(key)
        for index, kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
                print("del", index)
                del self.arr[arr_index][index]


if __name__== '__main__':
        t= hash()
        t["march 6"] = 310
        t["march 7"] = 420
        t["march 24"] = 31
        t["April 20"] = 460
        t["May 5"] = 315
        t["march 7"] = 420
        t.print_hash_table()
