# Define an iterable collection
class MyCollection:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __iter__(self):
        return MyIterator(self)


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


# Using the iterator pattern
if __name__ == "__main__":
    collection = MyCollection()
    collection.add_item("Item 1")
    collection.add_item("Item 2")
    collection.add_item("Item 3")

    iterator = iter(collection)

    print("Iterating through collection:")
    for item in collection:
        print(item)
