class FootballMatch:
    def __init__(self, stadium: str, goals: int, winner: str):
        if not isinstance(stadium, str):
            raise TypeError('Стадион должен быть строкой')
        self.stadium = stadium
        if goals < 0:
            raise ValueError('Нельзя забить меньше нуля')
        self.goals = goals
        if not isinstance(winner, str):
            raise TypeError('Победитель должен быть строкой')
        self.winner = winner
    def teams(self, red: int):
        if not isinstance(red, int):
            raise TypeError("Количество красных карточек должно быть числом")
        if red < 0:
            raise ValueError("Количесвто красных карточек не может быть меньше нуля")
        self.red = red

class History:  #Класс для исторических событий
    def __init__(self, year: int, place: str, members: str):
        if not isinstance(year, int):
            raise TypeError('Год события должен быть числом')
        self.year = year
        if not isinstance(place, str):
            raise TypeError('Место события должно быть строкой')
        self.place = place
        if not isinstance(members, str):
            raise ValueError('Участники должны быть строкой')
        self.members = members
    def country(self, nation:int):
        if not isinstance(nation, str):
            raise TypeError("Страна должна быть строкой")
        self.nation = nation

class Subject:
    def __init__(self, exam: str, duration: int):
        if not isinstance(exam, str):
            raise TypeError('Экзамен должен быть строкой')
        self.exam = exam
        if duration <= 0:
            raise ValueError('Продолжительность должна быть больше нуля')
        self.duration = duration
    def mark(self, grade:int):
        if not isinstance(grade, str):
            raise TypeError('Оценка должна быть строкой')
        if grade <= 0:
            raise ValueError('Оценка должна быть больше нуля')
        self.grade = grade


if __name__ == "__main__":
    match = FootballMatch("Stamford Bridge", 5, "Chelsea")
    import doctest
    doctest.testmod()
    pass
