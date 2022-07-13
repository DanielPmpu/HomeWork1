from typing import Union

from heroes import Superman, ChuckNorris
from news import NewsMaker
from places import Kostroma, Tokyo


def save_the_place(hero: Union[Superman, ChuckNorris], place: Union[Kostroma, Tokyo], news_maker: NewsMaker):
    hero.find(place)
    hero.attack()
    if hero.can_use_ultimate_attack:
        hero.ultimate()
    news_maker.create_news(hero, place)


if __name__ == '__main__':
    save_the_place(Superman(), Kostroma(), NewsMaker())
    print('-' * 20)
    save_the_place(ChuckNorris(), Tokyo(), NewsMaker())
