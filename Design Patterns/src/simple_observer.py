# Define the Subject (Observable)
class Subject:
    def __init__(self):
        self._observers = []

    def register_observer(self, observer):
        self._observers.append(observer)

    def unregister_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)


# Define the Observer
class Observer:
    def update(self, message):
        print(f"Received message: {message}")


# Usage example
if __name__ == "__main__":
    # Create a subject
    subject = Subject()

    # Create observers
    observer1 = Observer()
    observer2 = Observer()

    # Register observers with the subject
    subject.register_observer(observer1)
    subject.register_observer(observer2)

    # Notify observers with a message
    subject.notify_observers("Hello, observers!")

    # Unregister an observer
    subject.unregister_observer(observer1)

    # Notify remaining observer
    subject.notify_observers("Another message")
