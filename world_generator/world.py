from typing import Optional, Set


class World:

    ground_level: Optional["Field"]
    objects: Set["Object"]

    def __init__(self):
        self.ground_level = None
        self.objects = set()


class Object:

    world: World

    def __init__(self, world: World):
        self.world = world
        self.world.objects.add(self)

    def tick(self):
        pass


class Field(Object):
    def get_value(x: float, y: float, time: int) -> float:
        return 0


class Locatable:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


class Ageable:
    age: int

    def __init__(self, age: int):
        self.age = age


class Tree(Locatable, Ageable, Object):
    def __init__(self, world: World, x: float, y: float):
        Locatable.__init__(self, x=x, y=y)
        Ageable.__init__(self, age=0)
        Object.__init__(self, world=world)
