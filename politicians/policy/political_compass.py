"""Текстовое представление политического компаса.

Ось ``left_right`` идёт от левых значений к правым, а ось ``freedom`` —
от авторитарных значений к либертарианским. Ожидаемый игровой диапазон обеих
осей — примерно от -10 до 10, но значения за его пределами тоже поддерживаются.
"""


class PoliticalCompass:
    # Границы проходят между условными целыми зонами компаса. Поэтому, например,
    # координата -8 попадает в крайнюю область, а -7 — в соседнюю с ней.
    _BAND_BORDERS = (-7.5, -4.5, -1.5, 1.5, 4.5, 7.5)

    # Строки: от авторитарных взглядов к либертарианским (freedom: -10 -> 10).
    # Столбцы: от левых взглядов к правым (left_right: -10 -> 10).
    _IDEOLOGIES = (
        (
            "большевизм",
            "национал-большевизм",
            "авторитарный социализм",
            "этатизм",
            "национал-социализм",
            "фашизм",
            "традиционализм",
        ),
        (
            "авторитарный коммунизм",
            "авторитарный социализм",
            "красный консерватизм",
            "этатизм",
            "национализм",
            "национал-консерватизм",
            "фашизм",
        ),
        (
            "социализм",
            "левый национализм",
            "левый национализм",
            "национал-демократия",
            "социальный консерватизм",
            "консерватизм",
            "национал-консерватизм",
        ),
        (
            "демократический социализм",
            "социал-демократия",
            "социал-демократия",
            "центризм",
            "неолиберализм",
            "либеральный консерватизм",
            "неоконсерватизм",
        ),
        (
            "демократический социализм",
            "социал-демократия",
            "социал-либерализм",
            "либеральная демократия",
            "классический либерализм",
            "классический либерализм",
            "либертарианский консерватизм",
        ),
        (
            "утопический социализм",
            "либертарианский социализм",
            "экосоциализм",
            "зелёная политика",
            "либертарианство",
            "агоризм",
            "минархизм",
        ),
        (
            "анархо-коммунизм",
            "анархо-синдикализм",
            "мутуализм",
            "классический анархизм",
            "анархо-индивидуализм",
            "анархо-индивидуализм",
            "анархо-капитализм",
        ),
    )

    def __init__(self, left_right, freedom):
        # Названия и смысл координат сохранены для совместимости со старым кодом.
        self.left_right, self.freedom = left_right, freedom

    @classmethod
    def _band_index(cls, value) -> int:
        """Возвращает номер одной из семи областей для значения оси."""
        for index, border in enumerate(cls._BAND_BORDERS):
            if value < border:
                return index
        return len(cls._BAND_BORDERS)

    def ideology_name(self) -> str:
        """Возвращает цельное название идеологии для текущей точки компаса."""
        freedom_band = self._band_index(self.freedom)
        left_right_band = self._band_index(self.left_right)
        return self._IDEOLOGIES[freedom_band][left_right_band]

    # Следующие четыре метода оставлены как совместимые помощники для тех мест
    # проекта, где отдельно показываются горизонтальная или вертикальная ось.
    # Для итогового политического взгляда используются to_str()/to_str_name().
    def left_right_str(self) -> str:
        if self.left_right < -8:
            return "коммунист"
        if self.left_right <= -6:
            return "социалист"
        if self.left_right <= -2:
            return "социал-демократ"
        if self.left_right <= 1:
            return "центрист"
        if self.left_right <= 4:
            return "либерал"
        if self.left_right < 8:
            return "консерватор"
        return "ультраправый"

    def liberal_str(self) -> str:
        if self.freedom <= -8:
            return "тоталитарист-"
        if self.freedom <= -5:
            return "автократичный "
        if self.freedom <= -2:
            return "этатист-"
        if self.freedom <= 2:
            return "умеренный "
        if self.freedom <= 5:
            return "демократ-"
        if self.freedom <= 8:
            return "либертарианец-"
        return "анархист-"

    def left_right_str_name(self) -> str:
        if self.left_right < -8:
            return "коммунизм"
        if self.left_right <= -6:
            return "социализм"
        if self.left_right <= -2:
            return "социал-демократия"
        if self.left_right <= 1:
            return "центризм"
        if self.left_right <= 4:
            return "либерализм"
        if self.left_right < 8:
            return "консерватизм"
        return "ультраправый"

    def liberal_str_name(self) -> str:
        if self.freedom <= -8:
            return "тоталитаризм-"
        if self.freedom <= -5:
            return "автократичный(ая) "
        if self.freedom <= -2:
            return "этатизм-"
        if self.freedom <= 2:
            return "умеренный(ая) "
        if self.freedom <= 5:
            return "демократ-"
        if self.freedom <= 8:
            return "либертарианство-"
        return "анархизм-"

    def to_str_name(self) -> str:
        """Совместимое имя метода: теперь возвращает единую идеологию."""
        return self.ideology_name()

    def to_str(self) -> str:
        """Возвращает единую идеологию вместо склейки названий двух осей."""
        return self.ideology_name()


if __name__ == "__main__":
    examples = (
        (-7, -7),
        (-4, 1),
        (5, 3),
        (7, -6),
        (-8, 8),
        (0, 0),
    )

    for left_right, freedom in examples:
        compass = PoliticalCompass(left_right, freedom)
        print(f"({left_right:>3}, {freedom:>3}) -> {compass.to_str()}")
