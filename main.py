class Person:
    def __init__(self, building):
        self.building = building
        print('{}にいる\n'.format(self.building.name))

    def move(self, building):
        self.building = building
        print('{}に移動した'.format(self.building.name))

    def eat(self):
        print('{}を食べた\n'.format(self.building.serve()))

    def study(self):
        if self.building.has_teacher:
            print('{} を勉強した．\n'.format(self.building.teach()))

    def sleep(self):
        if self.building.has_bed:
            print('もう夜だ．おやすみ!\n')


class Home:
    has_bed = True

    def __init__(self):
        self.name = 'マイホーム'


class KyoyoTo():
    has_teacher = True

    def __init__(self):
        self.name = '教養棟'

    def teach(self):
        return input('受けたい授業名を入力してください\n')


class Restaurant:
    def __init__(self):
        self.name = ''
        self.menu = ''

    def serve(self):
        return self.menu


class HokuShoku(Restaurant):
    def __init__(self):
        self.name = '北部食堂'
        self.menu = 'ビュッフェ'


class Chuo(Restaurant):
    def __init__(self):
        self.name = '中央食堂'
        self.menu = 'スープカレー'


def player_move(player):
    option = [None, KyoyoTo(), HokuShoku(), Chuo()]
    while True:
        key = input(
            'どこに移動しますか？ 1.{} 2.{} 3.{}\n'.format(
                option[1].name, option[2].name, option[3].name))
        try:
            player.move(option[int(key)])
            break
        except BaseException:
            print('無効な入力です!\n')


def main(player):
    count = 0
    while count < 3:
        player_move(player)
        if player.building.name == '教養棟':
            player.study()
        else:
            player.eat()
        count += 1
    player.move(Home())
    player.sleep()


if __name__ == "__main__":
    ore = Person(Home())
    main(ore)
