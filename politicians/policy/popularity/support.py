class Support:
    def __init__(self, media, oligarchs, military, foreign, religious):
        self.media:int = media
        self.oligarchs:int = oligarchs
        self.military:int = military
        self.foreign:int = foreign
        self.religious:int = religious

    def check(self):
        self.media = min(100, max(self.media, 0))
        self.oligarchs = min(100, max(self.oligarchs, 0))
        self.military = min(100, max(self.military, 0))
        self.foreign = min(100, max(self.foreign, 0))
        self.religious = min(100, max(self.religious, 0))

    def total(self):
        return int((self.religious + self.media + self.foreign + self.military + self.oligarchs) / 5)

    def to_str_name(self):
        avg = self.total()

        if avg >= 80:
            return "Влиятельный игрок"
        if avg >= 60:
            return "Видная фигура"
        if avg >= 40:
            return "Принимают в счет"
        if avg >= 20:
            return "Маргинал"
        return "Изгой"

    def to_status(self):
        l = []

        if self.media >= 80:
            l.append("хозяин эфира")
        elif self.media <= 20:
            l.append("медийный невидимка")

        if self.oligarchs >= 80:
            l.append("карманный олигарх")
        elif self.oligarchs <= 20:
            l.append("чужой для бизнеса")

        if self.military >= 80:
            l.append("генеральский любимчик")
        elif self.military <= 20:
            l.append("презренный пацифист")

        if self.foreign >= 80:
            l.append("иностранный партнёр")
        elif self.foreign <= 20:
            l.append("враг иностранцев")

        if self.religious >= 80:
            l.append("помазанник божий")
        elif self.religious <= 20:
            l.append("безбожник")

        return l

    def to_str(self):
        return (f"{self.to_str_name()}:\n"
                f"- медиа: {self.media}%\n"
                f"- олигархи: {self.oligarchs}%\n"
                f"- военные: {self.military}%\n"
                f"- иностранцы: {self.foreign}%\n"
                f"- религия: {self.religious}%\n"
                f"- итоговая помощь: {self.total()}%\n" +
                f"статусы: {", ".join(self.to_status())}"
                )