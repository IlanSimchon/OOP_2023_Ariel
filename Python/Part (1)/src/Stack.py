class Stack:
    def __init__(self):
        self.elements = []
        self.counter = 0

    def push(self, val):
        self.elements.insert(0, val)
        self.counter += 1

    def pop(self):
        if self.counter > 0:
            self.elements.pop(0)
        else:
            raise Exception("The stack is empty")

    def top(self):
        if self.counter > 0:
            return self.elements[0]
        else:
            raise Exception("The stack is empty")

    def __iter__(self):
        self.current = -1
        return self

    def __next__(self):
        self.current += 1
        if self.current < self.counter:
            return self.elements[self.current]
        else:
            del self.current


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.push(6)
    s.push(7)
    s.push(8)
    it = s.__iter__()
    print(next(it))
