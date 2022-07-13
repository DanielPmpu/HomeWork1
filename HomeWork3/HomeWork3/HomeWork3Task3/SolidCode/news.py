class NewsMaker:

    @staticmethod
    def create_news(hero, place):
        place_name = getattr(place, 'name', 'place')
        print(f'{hero.name} saved the {place_name}!')
