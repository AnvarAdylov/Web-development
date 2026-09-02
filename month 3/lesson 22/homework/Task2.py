class Book:
    def __init__(self, title, author=None, year=None):
        self.title = title
        self.author = author
        self.year = year

    def display(self):
        title_aligned = self.title.ljust(30)
        print(title_aligned, end='')
        if self.author is not None:
            author_aligned = self.author.ljust(20)
            print(author_aligned, end='')
        else:
            author_aligned = ''.ljust(20)
            print(author_aligned, end='')
        if self.year is not None:
            year_aligned = str(self.year).rjust(5)
            print(year_aligned)
        else:
            year_aligned = ''.rjust(5)
            print(author_aligned, end='')
