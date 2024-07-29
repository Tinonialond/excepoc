class LinearHashing:
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None] * capacity

    def put(self, key, value):
        index = hash(key) % self.capacity
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            self.table[index].append((key, value))

    def get(self, key):
        index = hash(key) % self.capacity
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        return None

    def remove(self, key):
        index = hash(key) % self.capacity
        if self.table[index] is not None:
            self.table[index] = [(k, v) for k, v in self.table[index] if k != key]
