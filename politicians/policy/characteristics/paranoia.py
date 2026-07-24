import politicians.policy.characteristics.characteristic as ch
import random

class Paranoia(ch.Characteristic):
    """У паранойи есть уровень: от 0 до 100
    Если уровень паранойи доходит до 100, то он сходит с ума,
    И его отправляют в психушку, что равносильно поражению

    Каждый месяц паранойя увеличивается на 1
    Понижать уровень паранойи можно благодаря:
    - убрать или заменить кого-то из своего окружения
    - участвовать на парадах, где поддерживают твои взгляды
    - тратиться на психологов
    """

    name = "Паранойя"
    bio = "параноически боится, что его убьют или арестуют"

    level = 0

    def kill(self):
        return self.level >= 100

    def new_month(self):
        self.level = min(self.level + 2, 100)

    def tranquility(self, lvls):
        self.level = max(self.level - random.randint(3, 5) * lvls, 0)

    def anxiety(self, lvls):
        self.level = min(100, self.level + random.randint(2, 4) * lvls)