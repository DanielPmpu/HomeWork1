from abc import ABC, abstractmethod

from antagonistfinder import AntagonistFinder


class SuperHero(ABC):

    @abstractmethod
    def find(self, place):
        pass

    @abstractmethod
    def attack(self):
        pass


class SuperHeroWithUltimatePower(ABC):

    @abstractmethod
    def ultimate(self):
        pass


class ShooterMixin:

    @staticmethod
    def fire_a_gun():
        print('PIU PIU')


class InceneratorMixin:

    @staticmethod
    def incinerate_with_lasers():
        print('Wzzzuuuup!')


class KickerMixin:

    @staticmethod
    def kick():
        print('Kick')


class BrawlerMixin:

    @staticmethod
    def roundhouse_kick():
        print('Bump')


class Superman(KickerMixin, InceneratorMixin, SuperHeroWithUltimatePower, SuperHero):

    def __init__(self, name='Clark Kent', can_use_ultimate_attack=True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack
        self.finder = AntagonistFinder()

    def find(self, place):
        self.finder.get_antagonist(place)

    def attack(self):
        return self.kick()

    def ultimate(self):
        self.incinerate_with_lasers()


class ChuckNorris(BrawlerMixin, ShooterMixin, SuperHero):

    def __init__(self, name='Chuck Norris', can_use_ultimate_attack=False):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack
        self.finder = AntagonistFinder()

    def find(self, place):
        self.finder.get_antagonist(place)

    def attack(self):
        return self.fire_a_gun()
