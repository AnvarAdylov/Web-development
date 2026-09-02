
class Library:
    def __init__(self, name, book_list=None):
        self.name = name
        if book_list is None:
            book_list = []
        self.book_list = book_list

    def list(self):
        title_aligned = 'Название'.ljust(30)
        print(title_aligned, end='')
        author_aligned = 'Автор'.ljust(20)
        print(author_aligned, end='')
        year_aligned = 'Год'.rjust(5)
        print(year_aligned)
        for item in self.book_list:
            item.display()

    def filter(self, title=None, author=None, year=None):
        filtered = self.book_list

        if title is not None:
            filtered = [book for book in filtered if book.title == title]
        if author is not None:
            filtered = [book for book in filtered if book.author == author]
        if year is not None:
            filtered = [book for book in filtered if book.year == year]

        return filtered

    def add_book(self, book):
        self.book_list.append(book)

    def delete_book(self, book):
        self.book_list.pop(book)

    @staticmethod
    def as_table(book_list):
        title_aligned = 'Название'.ljust(30)
        print(title_aligned, end='')
        author_aligned = 'Автор'.ljust(20)
        print(author_aligned, end='')
        year_aligned = 'Год'.rjust(5)
        print(year_aligned)
        for item in book_list:
            item.display()
