import random
import politicians.policy.political_compass as pol_com
import politicians.policy.characteristics.characteristic as ch
import politicians.policy.characteristics.charisma as charisma
import politicians.policy.characteristics.poor_health as poor_health
import politicians.policy.job_title.base_job_title as bjt
import politicians.policy.job_title.deputy as deputy
import politicians.policy.job_title.president as president
import politicians.policy.popularity.popularity_indicator as pi
import politicians.policy.popularity.support as p_support
from hints.int_to_str import int_to_str
import politicians.nation.base_nationality as base_nationality

def str_years(year):
    year = year % 100
    if year == 0:   return "лет"
    if year == 1:   return "год"
    if year <= 4:   return "года"
    if year <= 20:  return "лет"
    if year % 10 == 0:   return "лет"
    if year % 10 == 1:   return "год"
    if year % 10 <= 4:   return "года"
    return "лет"

class Politician:
    def __init__(self, name, year, political_compass, characteristics, money, alive, at_large,
                 position, popularity, support, mind, old_age, track, location, citizenship,
                 place_of_residence, nationality:base_nationality.Nationality, political_hour,
                 name_party=None, nickname=None, bio=None):
        self.name:str = name
        self.nickname:str = nickname # псевдоним, None - его нет
        self.year:int = year
        self.political_compass:pol_com.PoliticalCompass = political_compass
        self.characteristics:list[ch.Characteristic] = characteristics
        self.alive:bool = alive
        self.at_large:bool = at_large
        self.position:bjt.BaseJobTitle = position
        self.name_party:str = name_party # в какой партии состоит, None - значит не состоит в партии
        self.old_age:int = old_age
        self.money:int = money
        self.mind:int = mind # чем выше уровень,
        # тем выше разнообразие вариантов ответа и тем лучше последствия ответов
        self.popularity: pi.Popularity = popularity
        self.bio:str = bio
        self.support:p_support.Support = support
        self.track:int = track
        self.location:str = location # где он находится прям сейчас
        self.citizenship:list[str] = citizenship
        self.place_of_residence:list[str] = place_of_residence
        self.nationality:base_nationality.Nationality = nationality
        self.political_hour = political_hour

    def to_briefly_str(self):
        return (f"{self.name}" + ("" if self.nickname is None else f" ({self.nickname})") +
                f" - {self.political_compass.to_str()}" +
                f"\nВозраст: {self.year} {str_years(self.year)}\n"
                f"Статус: {'жив' if self.alive else 'мертв'},"
                f" {"на свободе" if self.at_large else "сидит в тюрьме"}\n"
                f"Должность: {self.position.name}\n"
                f"{"Не с" if self.name_party is None else "С"}остоит "
                f"в партии{ "" if self.name_party is None else " " + str(self.name_party)}\n"
                f"Национальность: {self.nationality.to_str()}\n"
                f"Денег: {int_to_str(self.money)}\n"
                f"{"" if self.bio is None else '\nБиография: ' + self.bio}")

    def to_str(self) -> str:
        """Возвращает информацию о политике в текстовом виде

        пример:
            Владимир Ульянов Ильич (Ленин) - автократичный коммунист
            Возраст: 52 года
            Статус: мертв, на свободе
            Должность: президент
            Состоит в партии Большевики
            Денег: 10000
            Характеристики:
            - плохое здоровье: раньше начинает стареть
            - харизма: на публике его любят, больше слушают, сильнее доверяют
            Нейтральное отношение:
            - молодежь: 50%
            - люди среднего возраста: 60%
            - пожилые: 70%
            - элиты: 90%
            - бедные: 80%
            - богатые: 0%
            - суммарный рейтинг: 52%
            - рейтинг с элитами: 58%
            статусы: народный заступник, изгой олигархата, икона для элит, на поводке у власти
            Принимают в счет:
            - медиа: 90%
            - олигархи: 50%
            - военные: 99%
            - иностранцы: 15%
            - религия: 15%
            - итоговая помощь: 53%
            статусы: хозяин эфира, генеральский любимчик, враг иностранцев, безбожник
            Биография: устроил революцию в РИ
        """

        return (f"{self.name}" + ("" if self.nickname is None else f" ({self.nickname})") +
                f" - {self.political_compass.to_str()}" +
                f"\nВозраст: {self.year} {str_years(self.year)}\n"
                f"Статус: {'жив' if self.alive else 'мертв'},"
                f" {"на свободе" if self.at_large else "сидит в тюрьме"}\n"
                f"Должность: {self.position.name}\n"
                f"{"Не с" if self.name_party is None else "С"}остоит "
                f"в партии{ "" if self.name_party is None else " " + str(self.name_party)}\n"
                f"Национальность: {self.nationality.to_str()}\n"
                f"Денег: {int_to_str(self.money)}\n" +
                "Характеристики:\n" +
                f"\n".join(['- ' + char.to_str().lower() for char in self.characteristics]) +
                f"\n{self.popularity.to_str()}"
                f"\n{self.support.to_str()}"
                f"\nПолитических часов: {self.political_hour}"
                f"{"" if self.bio is None else '\nБиография: ' + self.bio}")

    def to_str2(self) -> str:
        return (f"{self.name}" + ("" if self.nickname is None else f" ({self.nickname})") +
                f"\n{self.political_compass.to_str()}" +
                f"\nВозраст: {self.year} {str_years(self.year)}\n"
                f"Статус: {'жив' if self.alive else 'мертв'},"
                f" {"на свободе" if self.at_large else "сидит в тюрьме"}\n"
                f"Должность: {self.position.name}\n"
                f"{"Не с" if self.name_party is None else "С"}остоит "
                f"в партии{"" if self.name_party is None else " " + str(self.name_party)}\n"
                f"Национальность: {self.nationality.to_str()}\n"
                f"Денег: {int_to_str(self.money)}\n" +
                "Характеристики:\n- " +
                f", ".join([char.name.lower() for char in self.characteristics]) +
                f"\n{self.popularity.to_str2()}"
                f"\n{self.support.to_str2()}"
                f"\nПолитических часов: {self.political_hour}"
                )

    def new_month(self):
        for char in self.characteristics:
            char.new_month()
        if self.at_large:
            self.money += self.position.get_money()
        self.check_kill()

    def is_old(self) -> bool:
        return self.old_age <= self.year

    def heart_attack(self) -> bool:
        return random.randint(1, 10) == 1 and self.is_old()

    def new_year(self):
        self.year += 1

        if self.is_old():
            if self.heart_attack():
                self.alive = False
            self.mind -= 1

    def start(self):
        for char in self.characteristics:
            char.start()
        self.check_health()

    def check_health(self):
        for char in self.characteristics:
            self.old_age += char.check_health()

    def check_clever(self):
        for char in self.characteristics:
            self.mind += char.check_mind()

    def check_kill(self):
        if not self.alive:
            return True
        for char in self.characteristics:
            if char.kill():
                self.alive = False
                return True

        return False

    def find(self, val:str):
        if val.lower() in self.to_str().lower():
            return True
        return False

if __name__ == "__main__":
    politician = Politician("Владимир Ульянов Ильич", 52, pol_com.PoliticalCompass(-9, -6),
                     [poor_health.PoorHealth(), charisma.Charisma()], 10000,False,
                      True, president.President(),
                        pi.Popularity(50, 60, 70, 90, 80, 0),
                            p_support.Support(90, 50, 99, 15, 15),
                            100, 60, 0, "Москва", ["СССР"],
                 ["Москва", "Ленинград"], base_nationality.Nationality("русский"), 100,
                      "Большевики", "Ленин", "устроил революцию в РИ")

    print(politician.to_str())

    print(politician.find("52 года")) # True
