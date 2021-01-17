class MyArray:
    def __init__(self):
        self.length = 0
        # Why use a dictionary to store the data
        # TODO: check array implementation in Python
        self.data = {}

    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data[self.length] = item
        self.length += 1
        return self.length

    def pop(self):
        del self.data[self.length-1]
        self.length -= 1
        return self.data[self.length-1]

    def delete(self, index):
        self.shift_items_v2(index)


    def shift_items_v1(self, index):
        for i in range(self.length - 1):
            if i == index:
                # should be present here as if i delete it will
                # be replaced by next, and i have no way of modifying index
                # del self.data[i]
                self.data[i] = self.data[i+1]
                del self.data[self.length - 1]
                self.length -= 1
            else:
                print('Not found')

    def shift_items_v2(self, index):
        # More elegant approach
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        del self.data[self.length - 1]
        self.length -= 1
