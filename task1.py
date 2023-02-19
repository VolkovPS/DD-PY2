if __name__ == "__main__":
    pass
class Sport_event:
    """Базовый класс спортивных событий"""
    def __init__(self, name:str, team1:str, team2:str):
        """Инициализатор класса"""
        self.name = name
        self.team1 = team1
        self.team2 = team2

    def __str__(self):
        """Магический метод, возвращающий строковый объект"""
        return f"Соревнование: {self.name}. Участники: {self.team1} и {self.team2}"

    def __repr__(self):
        """Информационная строка об объекте"""
        return f"{self.__class__.__name__}(Соревнование={self.name!r}, команда 1 ={self.team1!r}, команда 2 ={self.team2!r})"

class Football_event(Sport_event):
    """Дочерний класс спортивных событий"""
    def __init__(self,name:str, team1:str, team2:str, goals:int):
        """Инициализатор класса"""
        self.name = name
        self.team1 = team1
        self.team2 = team2
        self.goals = goals

    def __str__(self):
        """Магический метод, возвращающий строковый объект"""
        return f"Вид спорта: {self.name}. Участники: {self.team1} и {self.team2}." \
               f"Количество голов {self.goals}"  #Добавлено количество голов

    def __eq__(self, other):
        """Метод, сравнивающий события"""
        ...

class Tennis_event(Sport_event):
    """Дочерний класс спортивных событий"""
    def __init__(self,name:str, team1:str, team2:str, duration:float):
        """Инициализатор класса"""
        self.name = name
        self.team1 = team1
        self.team2 = team2
        self.duration = duration
