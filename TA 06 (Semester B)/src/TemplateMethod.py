from abc import ABC, abstractmethod


# Abstract class defining the template method
class BeverageTemplate(ABC):

    def prepare_beverage(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    @abstractmethod
    def boil_water(self):
        pass

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def pour_in_cup(self):
        pass

    @abstractmethod
    def add_condiments(self):
        pass


# Concrete class for preparing Coffee
class Coffee(BeverageTemplate):

    def boil_water(self):
        print("Boiling water for coffee")

    def brew(self):
        print("Brewing coffee grounds")

    def pour_in_cup(self):
        print("Pouring coffee into cup")

    def add_condiments(self):
        print("Adding sugar and milk to coffee")


# Concrete class for preparing Tea
class Tea(BeverageTemplate):

    def boil_water(self):
        print("Boiling water for tea")

    def brew(self):
        print("Steeping the tea")

    def pour_in_cup(self):
        print("Pouring tea into cup")

    def add_condiments(self):
        print("Adding lemon to tea")


# Concrete class for preparing FreshTea without condiments
class FreshTea(BeverageTemplate):

    def boil_water(self):
        print("Boiling water for fresh tea")

    def brew(self):
        print("Steeping the fresh tea leaves")

    def pour_in_cup(self):
        print("Pouring fresh tea into cup")

    def add_condiments(self):
        pass  # No condiments for fresh tea


# Concrete class for preparing Espresso without sugar and milk
class Espresso(BeverageTemplate):

    def boil_water(self):
        print("Boiling water for espresso")

    def brew(self):
        print("Brewing espresso grounds")

    def pour_in_cup(self):
        print("Pouring espresso into cup")

    def add_condiments(self):
        pass  # No sugar and milk for espresso


# Client code using the template method
def main():
    coffee = Coffee()
    print("Preparing Coffee:")
    coffee.prepare_beverage()

    print("\n")

    tea = Tea()
    print("Preparing Tea:")
    tea.prepare_beverage()

    print("\n")

    fresh_tea = FreshTea()
    print("Preparing Fresh Tea:")
    fresh_tea.prepare_beverage()

    print("\n")

    espresso = Espresso()
    print("Preparing Espresso:")
    espresso.prepare_beverage()


if __name__ == "__main__":
    main()
