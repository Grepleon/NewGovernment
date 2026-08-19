class PoliticalCompass:
    def __init__(self, left_right, freedom):
        self.left_right, self.freedom = left_right, freedom
        
    def left_right_str(self) -> str:
        if self.left_right < -8:
            return "коммунист"
        elif self.left_right <= -6:
            return  "социалист"
        elif self.left_right <= -2:
            return  "социал-демократ"
        elif self.left_right <= 1:
            return  "центрист"
        elif self.left_right <= 4:
            return  "либерал"
        elif self.left_right < 8:
            return  "консерватор"
        else:
            return  "ультраправый"
    
    def liberal_str(self) -> str:
        if self.freedom <= -8:
            return  "тоталитарист-"
        elif self.freedom <= -5:
            return  "автократичный "
        elif self.freedom <= -2:
            return  "этатист-"
        elif self.freedom <= 2:
            return  "умеренный "
        elif self.freedom <= 5:
            return  "демократ-"
        elif self.freedom <= 8:
            return  "либертарианец-"
        else:
            return  "анархист-"

    def left_right_str_name(self) -> str:
        if self.left_right < -8:
            return "коммунизм"
        elif self.left_right <= -6:
            return "социализм"
        elif self.left_right <= -2:
            return "социал-демократия"
        elif self.left_right <= 1:
            return "центризм"
        elif self.left_right <= 4:
            return "либерализм"
        elif self.left_right < 8:
            return "консерватизм"
        else:
            return "ультраправый"

    def liberal_str_name(self) -> str:
        if self.freedom <= -8:
            return "тоталитаризм-"
        elif self.freedom <= -5:
            return "автократичный(ая) "
        elif self.freedom <= -2:
            return "этатизм-"
        elif self.freedom <= 2:
            return "умеренный(ая) "
        elif self.freedom <= 5:
            return "демократ-"
        elif self.freedom <= 8:
            return "либертарианец-"
        else:
            return "анархизм-"

    def to_str_name(self):
        return self.liberal_str_name() + self.left_right_str_name()

    def to_str(self) -> str:
        word1 = "некий"
        word2 = "некто"
        
        word1 = self.liberal_str()
        word2 = self.left_right_str()

        

        return word1 + word2


if __name__ == "__main__":
    print(PoliticalCompass(5, 3).to_str())
    print(PoliticalCompass(-9, -7).to_str())
    print(PoliticalCompass(0,0).to_str())
    print(PoliticalCompass(10,-10).to_str())