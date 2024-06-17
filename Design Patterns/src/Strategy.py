# Define the strategy interface
class PaymentStrategy:
    def pay(self, amount):
        pass


# Implement concrete strategies
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} using credit card")


class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} using PayPal")


class BitcoinPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} using Bitcoin")


# Context class that uses a strategy
class ShoppingCart:
    def __init__(self, payment_strategy):
        self.items = []
        self.payment_strategy = payment_strategy

    def add_item(self, item):
        self.items.append(item)

    def checkout(self):
        total_amount = sum(item['price'] for item in self.items)
        self.payment_strategy.pay(total_amount)


# Client code
if __name__ == "__main__":
    # Create concrete strategy instances
    credit_card_payment = CreditCardPayment()
    paypal_payment = PayPalPayment()
    bitcoin_payment = BitcoinPayment()

    # Use strategies in the context
    cart1 = ShoppingCart(credit_card_payment)
    cart1.add_item({'product': 'Laptop', 'price': 1000})
    cart1.add_item({'product': 'Mouse', 'price': 20})
    cart1.checkout()

    cart2 = ShoppingCart(paypal_payment)
    cart2.add_item({'product': 'Headphones', 'price': 50})
    cart2.add_item({'product': 'Keyboard', 'price': 30})
    cart2.checkout()

    cart3 = ShoppingCart(bitcoin_payment)
    cart3.add_item({'product': 'Smartphone', 'price': 500})
    cart3.add_item({'product': 'Tablet', 'price': 300})
    cart3.checkout()
