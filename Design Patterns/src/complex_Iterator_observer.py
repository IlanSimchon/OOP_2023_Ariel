# Define an iterable collection
class MyCollection:
    def __init__(self):
        self.items = []
        self.observers = []

    def add_item(self, item):
        self.items.append(item)
        self.notify_observers()

    def remove_item(self, item):
        self.items.remove(item)
        self.notify_observers()

    def __iter__(self):
        iterator = MyIterator(self)
        self.observers.append(iterator)  # Add new iterator as observer
        return iterator

    def notify_observers(self):
        for observer in self.observers:
            observer.update()


# Define an iterator for the collection
class MyIterator:
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.collection.items):
            item = self.collection.items[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration

    def update(self):
        self.index = 0


# Using the iterator pattern with observer
if __name__ == "__main__":
    collection = MyCollection()
    collection.add_item("Item 1")
    collection.add_item("Item 2")
    collection.add_item("Item 3")

    iterator1 = iter(collection)
    iterator2 = iter(collection)
    iterator2.__next__()
    
    print("Iterating through collection with iterator1:")
    for item in iterator1:
        print(item)

    collection.remove_item("Item 2")

    print("\nIterating through collection with iterator1 after removal:")
    for item in iterator1:
        print(item)

    print("\nIterating through collection with new iterator2:")
    for item in iterator2:
        print(item)
