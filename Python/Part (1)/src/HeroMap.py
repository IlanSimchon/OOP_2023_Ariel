from Hero import Hero


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        return str(self.x) + ", " + str(self.y)


class Area:
    def __init__(self, p: Point, radius: float):
        self.center = p
        self.radius = radius

    def __repr__(self):
        return "(("+str(self.center)+"),\t" + str(self.radius)+")"


class HeroMap:
    def __init__(self):
        self.map = dict()

    # In order to use Hero object as keys, we have to make it hashable by implementing __hash__ function in Hero class

    def add_hero(self, h: Hero, a: Area):
        self.map[h] = a

    def __len__(self):
        return len(self.map)

    def __iter__(self):
        return self.map.__iter__()

    def get_heroes(self):
        return self.map.keys()

    def get_areas(self):
        return self.map.values()

    def get_pairs(self):
        return self.map.items()

    def contains(self, h: Hero):
        return self.map.get(h) is not None

    def get(self, h: Hero):
        return self.map.get(h)


if __name__ == '__main__':
    h1 = Hero("Batman", 100)
    h2 = Hero("Superman", 200)
    h3 = Hero("GreenLantern", 150)
    h4 = Hero("WonderWoman", 180)
    h5 = Hero("Batgirl", 120)
    h6 = Hero("Batkid", 90)
    a1 = Area(Point(0, 0), 5)
    a2 = Area(Point(40, 28), 5)
    a3 = Area(Point(13, 4), 5)
    a4 = Area(Point(9, 63), 5)
    a5 = Area(Point(48, 14), 5)
    a6 = Area(Point(19, 13), 5)
    map = HeroMap()
    map.add_hero(h1, a1)
    map.add_hero(h2, a2)
    map.add_hero(h3, a3)
    map.add_hero(h4, a4)
    map.add_hero(h5, a5)
    map.add_hero(h6, a6)
    print(map.get(h1))
    print(map.get(Hero("pc", 500)))
    for h in map:
        print(h)
