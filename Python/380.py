import random


class RandomizedSet:

    def __init__(self):
        self.data_set = []
        self.data_map = {}

    def insert(self, val: int) -> bool:
        if val in self.data_map:
            return False
        self.data_set.append(val)
        self.data_map[val] = len(self.data_set) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.data_map:
            return False
        last_element = self.data_set[-1]
        index_of_element_to_delete = self.data_map[val]

        # self.data_map[last_element] = index_of_element_to_delete
        self.data_set[index_of_element_to_delete] = last_element

        # self.data_set[-1] = val
        self.data_set.pop()
        self.data_map.pop(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.data_set)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
