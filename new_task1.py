class SportEvent:
    """Базовый класс спортивных событий"""
    def __init__(self, sport:str, place:str, time:str):
        """Инициализатор класса"""
        self.sport = sport  #Вид спорта
        self.place = place  #Местоположение соревнование
        self.time = time  #Время начала

    def __str__(self):
        """Магический метод, возвращающий строковый объект"""
        return f"Вид спорта: {self.sport}. Место: {self.place} Время начала: {self.time}"

    def __repr__(self):
        """Информационная строка об объекте"""
        return f"{self.__class__.__name__}(Вид спорта={self.sport!r}, место ={self.place!r}, время ={self.time!r})"

    def get_info(self) -> str:
        """Возвращает информацию о спортивном событии."""
        return f"Место: {self.place}. Время начала: {self.time}"

class FootballEvent(SportEvent):
    """Дочерний класс спортивных событий"""
    def __init__(self,tournament:str, team1:str, team2:str, goals:int):
        """Инициализатор класса"""
        self.tournament = tournament  #Название турнира
        self.team1 = team1  #Первая команда
        self.team2 = team2  #Вторая команда
        self.goals = goals  #Количество голов

    def __str__(self):
        """Магический метод, возвращающий строковый объект"""
        return f"Вид спорта: {self.sport}. Турнир: {self.tournament} Участники: {self.team1} и {self.team2}." \
               f"Количество голов: {self.goals}"  #Добавлено количество голов

    def get_info(self) -> str:
        """Возвращает информацию о футбольном событии."""
        return f"Турнир: {self.tournament}. Участники: {self.team1} и {self.team2}. Количество голов: {self.goals}"

class TennisEvent(SportEvent):
    """Дочерний класс спортивных событий"""
    def __init__(self, player1:str, player2:str, duration:float):
        """Инициализатор класса"""
        self.player1 = player1  #Первый участник
        self.player2 = player2  #Второй участник
        self.duration = duration  #Продолжительность игры

sport1 = SportEvent("Футбол", "РФ", "10 часов")
print(sport1)
