
BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

class Book:
    def __init__(self, id: int, name: str, pages: int):
        self.id = id  #Прописываем атрибуты экземпляра
        self.name = name
        self.pages = pages

    def __str__(self) -> str:  #Объявление метода __str__
        return f'Книга "{self.name}"'
    def __repr__(self) -> str:  #Объявление метода __repr__
        return f'Book(id_={self.id!r}, name={self.name!r}, pages={self.pages!r})'

class Library:
    def __init__(self, books = None):
        if books is None:  #Условие передачи аргумента
            self.books = []  #Инициализация библиотеки с пустым списком
        else:
            self.books = books
    def get_next_book_id(self):
        if not self.books:
            return 1
        else:
            return self.books[-1].id+1  #Возвращение идентификатора последней книги +1
    def get_index_by_book_id(self):
        for i, book in enumerate (self.books):
            if id == book.id:
                return i
            else:
                raise ValueError("Книги с запрашиваемым id не существует")




if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
