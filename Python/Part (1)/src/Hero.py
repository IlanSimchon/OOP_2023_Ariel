import functools

"""In order to create comparator of obejects we need to suppert both equals and less than operators, by doing
    that we can use sorted function and sort by "<" operator.
    In any case we would like to create a comparator that can compare by multiple parameters, like power, length of
    a string, lexicographically and anything else you can think of, we have to create our own comparator and implement
    the sort methods."""


class Hero:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    """Support the == operators between Hero objects"""

    def __eq__(self, other):
        if not isinstance(other, Hero):
            return False
        if self.name == other.name and self.power == other.power:
            return True
        return False

    """Support the < operator"""

    def __lt__(self, other):
        return self.power < other.power

    """Support "toString" of Hero object in python"""

    def __repr__(self):
        return "(" + self.name + ", " + str(self.power) + ")"

    def __str__(self):
        return "(" + self.name + "\t " + str(self.power) + ")"

    def __hash__(self):
        return hash(self.__repr__())


class HeroComparator:
    """collection is a list of heroes"""

    def __init__(self, collection):
        self.collection = collection

    """This function is a comparator of a collection of Hero objects. The function get the Integer compare type and
        return a sorted collection according to the compare type.
    """

    def sort_by_type(self, comp_type: int):
        if comp_type == 0:  # compare by power
            return sorted(self.collection)
        elif comp_type == 1:  # compare by the length of the name
            return sorted(self.collection, key=lambda x: len(x.name), reverse=False)
        elif comp_type == 2:  # compare lexicographically
            return sorted(self.collection, key=lambda x: x.name, reverse=False)
        elif comp_type == 3:  # compare by power and then lexicographically
            return sorted(self.collection, key=lambda x: (x.power, x.name), reverse=False)
        elif comp_type == 4:  # compare lexicographically and then by power
            return sorted(self.collection, key=lambda x: (x.name, x.power), reverse=False)
        else:  # not sort
            return self.collection


if __name__ == '__main__':
    h1 = Hero("Batman", 100)
    print(str(h1))
    print(h1.__str__())
    print(repr(h1))
    print(h1.__repr__())
    h2 = Hero("Superman", 200)
    h3 = Hero("GreenLantern", 150)
    h4 = Hero("WonderWoman", 180)
    h5 = Hero("Batgirl", 120)
    h6 = Hero("Batkid", 90)
    li = [h1, h2, h3, h4, h5, h6]
    print("original:")
    print(li)
    l = sorted(li)
    print("sort by power:")
    print(l)
    l2 = sorted(li, key=lambda x: len(x.name), reverse=False)
    print("sort by the length of the name:")
    print(l2)
    l3 = sorted(li, key=lambda x: str(x.name), reverse=False)
    print("lexicographically:")
    print(l3)
    hc = HeroComparator(li)
    print("default:")
    print(hc.sort_by_type(-1))
    print("Lexicographically")
    print(hc.sort_by_type(2))
    print("by power and then lexicographically")
    print(hc.sort_by_type(3))
    print("lexicographically and then by power")
    print(hc.sort_by_type(4))
