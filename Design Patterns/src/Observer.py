from abc import ABC, abstractmethod
from datetime import datetime


# Subject interface
class Sender(ABC):

    def __init__(self):
        self._members = []

    def register(self, member):
        self._members.append(member)

    def unregister(self, member):
        self._members.remove(member)

    def notify(self, newsletter):
        for member in self._members:
            member.update(newsletter)


# Observer interface
class Member(ABC):

    @abstractmethod
    def update(self, newsletter):
        pass


# Concrete implementation of Observer (Member)
class Person(Member):

    def __init__(self, name):
        self._name = name

    def update(self, newsletter):
        print(f"{self._name} received newsletter: {newsletter}")


# Concrete implementation of Subject (Sender)
class NewsletterPublisher(Sender):

    def send_newsletter(self, content):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        newsletter = f"{timestamp} - Newsletter: {content}"
        print(f"Sending newsletter: {newsletter}")
        self.notify(newsletter)


# Client code using the Observer pattern
def main_observer_example():
    # Create a newsletter publisher (subject)
    newsletter_publisher = NewsletterPublisher()

    # Create subscribers (observers)
    subscriber1 = Person("Alice")
    subscriber2 = Person("Bob")

    # Add subscribers to the newsletter publisher
    newsletter_publisher.register(subscriber1)
    newsletter_publisher.register(subscriber2)

    # Send a newsletter, and subscribers will be notified
    newsletter_publisher.send_newsletter("Latest Updates")


if __name__ == "__main__":
    main_observer_example()
