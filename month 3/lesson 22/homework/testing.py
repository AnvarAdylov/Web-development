import Task1
import Task2
import Task3
import Task1menu

print("Введите длину и ширину прямоугольника:")
length = int(input('> '))
width = int(input('> '))
recty = Task1.Rectangle(length, width)
whatever = Task1menu.menu(recty)
whatever.do_it()


book = Task2.Book('book', None, '1945')
book.display()

book_1 = Task2.Book('Чистый код', 'Дядя Боб', 2017)
book_2 = Task2.Book('От 2 до 5', 'Корней Чуковский', 1958)
book_3 = Task2.Book('Идеальный программист', 'Дядя Боб', 2018)
book_4 = Task2.Book('Рецепты татарской кухни', year=2018)
library = Task3.Library('Домашняя библиотека')
library.add_book(book_1)
library.add_book(book_2)
library.add_book(book_3)
library.add_book(book_4)
print(library.name)  # вывод названия
library.list()       # вывод книг
books = library.filter(author='Корней Чуковский', title='От 2 до 5')
books[0].display()
books = library.filter(author='Дядя Боб')
Task3.Library.as_table(books)  # вызов от имени класса
