class Popularity:
    def __init__(self, youth, middle_aged, elderly, in_power, poor, reach):
        self.youth:int = youth
        self.middle_aged:int = middle_aged
        self.elderly:int = elderly
        self.in_power: int = in_power
        self.poor = poor
        self.reach = reach

    def total(self):
        return int((self.youth + self.middle_aged + self.elderly + self.in_power + self.poor + self.reach) / 6)

    def peoples_total(self):
        return int((self.youth + self.middle_aged + self.elderly + self.poor + self.reach) / 5)

    def check(self):
        self.youth = min(100, max(self.youth, 0))
        self.middle_aged = min(100, max(self.middle_aged, 0))
        self.elderly = min(100, max(self.elderly, 0))
        self.in_power = min(100, max(self.in_power, 0))
        self.poor = min(100, max(self.poor, 0))
        self.reach = min(100, max(self.reach, 0))

    def for_poor(self, count):
        self.poor += count
        self.reach -= int(count / 2) + count % 2
        self.check()

    def for_reach(self, count):
        self.reach += count
        self.poor -= int(count / 2) + count % 2
        self.check()

    def for_youth(self, count):
        self.youth += count
        self.elderly -= int(count / 2) + count % 2
        self.check()

    def for_middle(self, count):
        self.middle_aged += count
        self.check()

    def for_elderly(self, count):
        self.youth -= int(count / 2) + count % 2
        self.elderly += count
        self.check()

    def add_peoples(self, count):
        self.youth += int(count / 3)
        self.middle_aged += count - 2 * int(count / 3)
        self.elderly += int(count / 3)
        self.check()

    def for_in_power(self, count):
        self.in_power += count
        self.add_peoples(-3 * count)
        self.check()

    def for_peoples(self, count):
        self.in_power -= int(count / 3)
        self.add_peoples(count)
        self.check()

    def to_str(self) -> str:
        return (f"{self.get_avg_status()}:"
                f"\n- молодежь: {self.youth}%"
                f"\n- люди среднего возраста: {self.middle_aged}%"
                f"\n- пожилые: {self.elderly}%"
                f"\n- элиты: {self.in_power}%"
                f"\n- бедные: {self.poor}%"
                f"\n- богатые: {self.reach}%"
                f"\n- суммарный рейтинг: {self.peoples_total()}%"
                f"\n- рейтинг с элитами: {self.total()}%"
                f"\nстатусы: {", ".join(self.get_str_status())}")

    def get_avg_status(self) -> str:
        avg = self.peoples_total()
        if avg >= 80:
            return "Народный любимчик"
        if avg >= 60:
            return "Уважаемый"
        if avg >= 40:
            return "Нейтральное отношение"
        if avg >= 20:
            return "Недолюбливают"
        return "Ненавидят"

    def get_str_status(self) -> list[str]:
        l = []

        if self.youth >= 80:
            l.append("молодежный любимчик")
        if self.middle_aged >= 80:
            l.append("кумир средних лет")
        if self.elderly >= 80:
            l.append("фаворит старой гвардии")

        if self.youth <= 20:
            l.append("потерял молодежь")
        if self.middle_aged <= 20:
            l.append("игнорируется средним классом")
        if self.elderly <= 20:
            l.append("предал пенсионеров")

        if self.poor >= 80:
            l.append("народный заступник")
        if self.poor <= 20:
            l.append("враг трудящихся")

        if self.reach >= 80:
            l.append("бизнес-герой")
        if self.reach <= 20:
            l.append("изгой олигархата")

        if self.in_power >= 80:
            l.append("икона для элит")
        if self.in_power <= 20:
            l.append("враг истеблишмента")

        if self.in_power > self.peoples_total() + 10:
            l.append("на поводке у власти")
        if self.in_power + 10 < self.peoples_total():
            l.append("народный трибун")

        if self.middle_aged >= 80 and self.in_power >= 80:
            l.append("свой среди своих")
        if self.peoples_total() >= 80 and self.in_power <= 20:
            l.append("гроза олигархов")
        if self.peoples_total() <= 20 and self.in_power >= 80:
            l.append("палач народа")

        if not l:
            l.append("серая мышь")

        return l


if __name__ == "__main__":
    pop = Popularity(80, 50, 20, 20, 70, 50)
    print(pop.to_str())
    pop.for_in_power(5)
    print(pop.to_str())
    pop.for_youth(6)
    print(pop.to_str())
    pop = Popularity(30, 60, 90, 100, 50, 80)
    print(pop.to_str())

