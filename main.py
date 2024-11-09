class Book:
    def __init__(self, book_name: str, release_date: str, count_pages: int, book_in_library: bool = True):
        try:
            if type(book_name) == str and type(release_date) == str and type(count_pages) == int and type(
                    book_in_library) == bool:
                self.__book_name = book_name
                self.__release_date = release_date
                self.__count_pages = count_pages
                self.__book_in_library = book_in_library
            else:
                raise TypeError('Были введены данные неверного типа (str, str, int, bool(Не обязательно))')
        except TypeError as Error:
            print(Error)
    def __str__(self):
        print(f'Книга: {self.__book_name}\nДата выпуска: {self.__release_date}\n В ней {self.__count_pages} страниц(ы)')
    def get_book_name(self):
        print(self.__book_name)
    def get_book_release_data(self):
        print(self.__release_date)
    def get_book_count_pages(self):
        print(self.__release_date)



class Library:
    __Books_in_library = 0
    __Books_list = list()
    __clients_base = dict()

    def add_new_book(self, book: Book):
        self.__Books_in_library += 1
        self.__Books_list.append(book)

    def give_book(self, book: Book, client: Client):
        self.__Books_in_library -= 1
        self.__Books_in_library.remove(book)
        if hash(client) in self.__clients_base.keys():
            self.__clients_base[hash(client)]['Books_in_usage'].append(book)
        else:
            self.__clients_base[hash(client)] = {'Name': client.name,
                                                 'Phone': client.phone,
                                                 'Age': client.age,
                                                 'Books_in_usage': [book]}

class People:
    pass

class Client(People):
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone