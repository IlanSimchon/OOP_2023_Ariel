from abc import ABC, abstractmethod


# Component interface
class TextPrinter(ABC):
    @abstractmethod
    def print_text(self):
        pass


# Concrete component
class SimpleTextPrinter(TextPrinter):
    def __init__(self, text):
        self._text = text

    def print_text(self):
        return self._text


# Decorator abstract class
class TextDecorator(TextPrinter, ABC):
    def __init__(self, text_printer):
        self._text_printer = text_printer

    @abstractmethod
    def print_text(self):
        pass


# Concrete decorators
class BoldTextDecorator(TextDecorator):
    def print_text(self):
        return "\033[1m" + self._text_printer.print_text() + "\033[0m"


class RedTextDecorator(TextDecorator):
    def print_text(self):
        return "\033[91m" + self._text_printer.print_text() + "\033[0m"


class UnderlineTextDecorator(TextDecorator):
    def print_text(self):
        return "\033[4m" + self._text_printer.print_text() + "\033[0m"


class ItalicTextDecorator(TextDecorator):
    def print_text(self):
        return "\033[3m" + self._text_printer.print_text() + "\033[0m"


# Client code
if __name__ == "__main__":
    # Create a simple text printer
    simple_text_printer = SimpleTextPrinter("Hello, World!")

    # Decorate the text printer with various decorators
    bold_text_printer = BoldTextDecorator(simple_text_printer)
    red_text_printer = RedTextDecorator(simple_text_printer)
    underline_text_printer = UnderlineTextDecorator(simple_text_printer)
    italic_text_printer = ItalicTextDecorator(simple_text_printer)


    # Print the decorated text
    print("Simple Text:")
    print(simple_text_printer.print_text())

    print("\nDecorated Texts:")
    print(bold_text_printer.print_text())
    print(red_text_printer.print_text())
    print(underline_text_printer.print_text())
    print(italic_text_printer.print_text())

