import random


class Person:
    def __init__(self, name, home):
        self.name = name
        self.home = home
        self.place = home
        print('{}は{}にいる'.format(self.name, home.name))

    def move(self, place):
        self.place = place
        print('{}は{}に移動した'.format(self.name, place.name))

    def do(self):
        print(self.place.recommend())


class Place:
    def __init__(self, name):
        self.name = name

    def recommend(self):
        raise NotImplementedError()


class Home(Place):
    def __init__(self, bed):
        super().__init__('自宅')
        self.bed = bed

    def recommend(self):
        return 'もう夜です\n{}で寝ます\nおやすみなさい'.format(self.bed)


class School(Place):
    def __init__(self):
        super().__init__('教養棟')

    def recommend(self):
        subject = input('受けたい授業名を入力してください:')
        return '{} を勉強した'.format(subject)


class Restaurant(Place):
    def __init__(self, name, menu):
        super().__init__(name)
        self.menu = menu

    def recommend(self):
        return random.choice(self.menu)


def main(player):
    places = (
        player.home,
        School(),
        Restaurant('北部食堂', ('定食', 'ラーメン', 'うどん', '蕎麦')),
        Restaurant('中央食堂', ('スープカレー', '牛丼', 'ハンバーガー'))
    )
    prompt = (
        '\nどこに移動しますか？ 0. 終了 ' +
        ' '.join(
            '{}.{}'.format(i, place.name) for i,
            place in enumerate(
                places,
                1)) + ':')
    while True:
        try:
            select = int(input(prompt))
        except BaseException:
            select = -1
        if select == 0:
            return
        if not 1 <= select <= len(places):
            print('無効な入力です')
            continue

        place = places[select - 1]
        player.move(place)
        player.do()


if __name__ == "__main__":
    main(Person('俺', Home('布団')))
