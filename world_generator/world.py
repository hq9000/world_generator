from dataclasses import dataclass
from typing import Optional, Set


@dataclass
class Point:
    x: float
    y: float
    z: float


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
    location: Point

    def __init__(self, p: Point):
        self.location = p


class Volumetric:
    p0: Point
    p1: Point
    p2: Point
    p3: Point
    p4: Point
    p5: Point
    p6: Point
    p7: Point

    def __init__(
        self,
        p0: Point,
        p1: Point,
        p2: Point,
        p3: Point,
        p4: Point,
        p5: Point,
        p6: Point,
        p7: Point,
    ):
        self.p0 = p0
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.p5 = p5
        self.p6 = p6
        self.p7 = p7


class Ageable:
    age: int

    def __init__(self, age: int):
        self.age = age


class Tree(Locatable, Ageable, Object):
    def __init__(self, world: World, x: float, y: float):
        Locatable.__init__(self, x=x, y=y)
        Ageable.__init__(self, age=0)
        Object.__init__(self, world=world)
