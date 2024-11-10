class People:
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone

class Client(People):
    def __init__(self, name, age, phone):
        super().__init__(name, age, phone)
        self.book_list = list()


class Book:
    def __init__(self, book_name: str, release_date: str, count_pages: int, book_in_library: bool = True):
        try:
            if (isinstance(book_name, str) and isinstance(release_date, str) and isinstance(count_pages,
                    int)) and isinstance(book_in_library, bool):
                self._book_name = book_name
                self._release_date = release_date
                self._count_pages = count_pages
                self.book_in_library = book_in_library
            else:
                raise TypeError('Были введены данные неверного типа (str, str, int, bool(Не обязательно))')
        except TypeError as Error:
            print(Error)

    def __repr__(self):
        return f'Книга: {self._book_name}'

    def __str__(self):
        return f'Книга: {self._book_name}\nДата выпуска: {self._release_date}\nВ ней {self._count_pages} страниц(ы)'

    def get_book_name(self):
        return self._book_name

    def get_book_release_data(self):
        return self._release_date

    def get_book_count_pages(self):
        return self._count_pages



class Library:
    _books_in_library = 0
    _books_list = list()
    _clients_base = dict()

    def add_new_book(self, book: Book):
        self._books_in_library += 1
        self._books_list.append(book)

    @staticmethod
    def check_book_in_library(book):
        return book.book_in_library

    def give_book(self, book: Book, client: Client):
        if self.check_book_in_library(book):
            self._books_in_library -= 1
            self._books_list.remove(book)
            book.book_in_library = False
            if hash(client) in self._clients_base.keys():
                self._clients_base[hash(client)]['Books_in_usage'].append(book)
            else:
                self._clients_base[hash(client)] = {'Name': client.name,
                                                     'Phone': client.phone,
                                                     'Age': client.age,
                                                     'Books_in_usage': [book]}
            client.book_list.append(book)
        else:
            print('Книга сейчас не находиться в библиотеке')

    def return_book(self, client, book):
            if book in self._clients_base[hash(client)]['Books_in_usage']:
                self._clients_base[hash(client)]['Books_in_usage'].remove(book)
                self._books_in_library += 1
                self._books_list.append(book)
                book.book_in_library = True
            else:
                print('У клиента нет этой книги')