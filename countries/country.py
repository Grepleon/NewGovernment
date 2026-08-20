import countries.areas.base_area as bc
import countries.cities.base_city as bcy
import countries.cities.location as loc
from hints.int_to_str import int_to_str

class Country:
    def __init__(self, name, name_capital, president, areas, ministry_of_finance, ministry_of_internal_affairs,
                 ministry_of_foreign_affairs, ministry_of_defence, ministry_of_social_policy, ministry_of_justice,
                 prime_minister, head_of_cb, budget, costs, color):
        self.name:str = name
        self.name_capital = name_capital
        self.areas:dict[str:bc.Area] = areas
        self.president:str = president

        self.ministry_of_finance:str = ministry_of_finance
        self.ministry_of_internal_affairs: str = ministry_of_internal_affairs
        self.ministry_of_foreign_affairs: str = ministry_of_foreign_affairs
        self.ministry_of_defence: str = ministry_of_defence
        self.ministry_of_social_policy: str = ministry_of_social_policy
        self.ministry_of_justice: str = ministry_of_justice
        self.prime_minister:str = prime_minister

        self.head_of_cb:str = head_of_cb

        self.budget:int = budget
        self.area_costs:dict[str:int] = costs

        self.color = color

    def to_str(self):
        """
        можно будет потом еще добавить регионы
        f"\nРегионы:\n" +
"\n".join(["- " + self.areas[area].name + ':\n' + "\n".join(['-- ' +
self.areas[area].cities[city].name for city in self.areas[area].cities]) for area in self.areas])
        """

        return (f"Государство \"{self.name}\":"
                f"\nСтолица: {self.name_capital}"
                f"\nПравитель: {self.president}"
                f"\nДолжностные лица:"
                f"\n- премьер-министр: {self.prime_minister}"
                f"\n- министр финансов: {self.ministry_of_finance}"
                f"\n- министр внутренних дел: {self.ministry_of_internal_affairs}"
                f"\n- министр иностранных дел: {self.ministry_of_foreign_affairs}"
                f"\n- министр обороны: {self.ministry_of_defence}"
                f"\n- министр социальной политики: {self.ministry_of_social_policy}"
                f"\n- министр юстиций: {self.ministry_of_justice}"
                f"\n- глава ЦБ: {self.head_of_cb}"
                f"\nБюджет: {int_to_str(self.budget)}"
                )



if __name__ == "__main__":
    print(Country("Государственное государство", "Государственная столица",
                  "Представитель государственной власти",
                  {"Столичная": bc.Area("Столичная",
    {"Гос-Стол": bcy.City("Гос-Стол", "Мэр", loc.Location(20, 58),
     {}, 5003, 20000)}, "Губернатор", {}, 500000)},
        "M1", "M2", "M3", "M4",
          "M5", "M6", "MM", "HC", 10000000,
                  {}).to_str())