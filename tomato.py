class Tomato:
    states = {
        'None': 0,
        'Flowering': 1,
        'Green': 2,
        'Red': 3
    }

    def __init__(self, index):
        self._index = index
        self._state = Tomato.states['None']

    def grow(self):
        if self._state < 3:
            self._state += 1

    def is_ripe(self):
        return self._state == 3

class TomatoBush:
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(num)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        for tomato in self.tomatoes:
            if not tomato.is_ripe():
                return False
        return True

    def give_away_all(self):
        self.tomatoes.clear()

class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print('Gardener is working...')
        self._plant.grow_all()
        for i, tomato in enumerate(self._plant.tomatoes):
            state = list(Tomato.states.keys())[list(Tomato.states.values()).index(tomato._state)]
            print(f'Tomato {i} is {state.lower()}')

    def harvest(self):
        if self._plant.all_are_ripe():
            print('Harvesting...')
            self._plant.give_away_all()
        else:
            print('Too early! Your plant is green and not ripe.')

    @staticmethod
    def knowledge_base():
        print('Harvest time for tomatoes should ideally occur\nwhen the fruit is a mature green and\nthen allowed to ripen off the vine.\nThis prevents splitting or bruising\nand allows for a measure of control over the ripening process.')

if __name__ == '__main__':
    Gardener.knowledge_base()

    bush = TomatoBush(3)
    gardener = Gardener('Pete', bush)

    gardener.work()
    gardener.harvest()

    gardener.work()
    gardener.harvest()

    gardener.work()
    gardener.harvest()
