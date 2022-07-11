from main import BooksCollector
import pytest
#@pytest.fixture()
import random
from essential_generators import DocumentGenerator
gen = DocumentGenerator()


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector

class TestBooksCollector:

    def test_init_books_ratings_is_empty_true(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # список books_rating который нам возвращает метод get_list_of_favorites_book, имеет длину 0
        assert len(collector.get_books_rating()) == 0

    def test_init_favorites_is_empty_true(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # список favorites, который нам возвращает метод get_list_of_favorites_book, имеет длину 2
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_book_was_added_have_rating_one(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу
        collector.add_new_book('Гордость и предубеждение и зомби')

        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 1
        # значение рейтинга, который нам возвращает метод get_book_rating, вернет 1
        assert len(collector.get_books_rating()) == 1
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 1

    def test_add_new_book_add_book_twice(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две одинаковые книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')

        # проверяем, что добавилась одна книга
        assert len(collector.get_books_rating()) == 1

    def test_set_book_rating_set_rating_in_range_one_ten(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу
        collector.add_new_book('Гордость и предубеждение и зомби')

        # добавляем рейтинг 5 книге
        collector.set_book_rating('Гордость и предубеждение и зомби', 5)

        # проверяем, что рейтинг равен 5
        # значение рейтинга, который нам возвращает метод get_book_rating, вернет 5
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 5

    def test_set_book_rating_set_rating_none_existing_book(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу
        collector.add_new_book('Гордость и предубеждение и зомби')

        # добавляем рейтинг книге, которой нет в словаре
        collector.set_book_rating('Униженные и оскорблённые', 5)

        # проверяем, что рейтинг вернется None
        # значение рейтинга,, который нам возвращает метод get_book_rating, вернет отсутствие книги
        assert collector.get_book_rating('Униженные и оскорблённые') == None


    def test_set_book_rating_set_rating_more_ten(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу
        collector.add_new_book('Гордость и предубеждение и зомби')

        # добавляем рейтинг книге
        collector.set_book_rating('Гордость и предубеждение и зомби', 11)

        # проверяем, что рейтинг равен дефолтной 1
        # значение рейтинга, которое нам возвращает метод get_book_rating, вернет 1
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 1

    def test_set_book_rating_set_rating_zero(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу
        collector.add_new_book('Гордость и предубеждение и зомби')

        # добавляем рейтинг книге
        collector.set_book_rating('Гордость и предубеждение и зомби', 0)

        # проверяем, что рейтинг равен дефолтной 1
        # значение рейтинга, которое нам возвращает метод get_book_rating, вернет 1
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 1

    def test_get_books_with_specific_rating_get_books_with_existing_rating(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем три книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Униженные и оскорблённые')

        # добавляем рейтинг книгам
        collector.set_book_rating('Гордость и предубеждение и зомби', 7)
        collector.set_book_rating('Что делать, если ваш кот хочет вас убить', 5)
        collector.set_book_rating('Униженные и оскорблённые', 5)

        # проверяем, что длина списка books_with_specific_rating с книгами, имеющими рейтиг 5, равна 2
        # названия книг в списке books_with_specific_rating соотвествуют тем, которые имеют рейтинг 5
        assert len(collector.get_books_with_specific_rating(5)) == 2
        assert 'Что делать, если ваш кот хочет вас убить' in collector.get_books_with_specific_rating(5)
        assert 'Униженные и оскорблённые' in collector.get_books_with_specific_rating(5)

    def test_get_books_with_specific_rating_get_book_with_none_existing_rating(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # добавляем рейтинг книгам
        collector.set_book_rating('Гордость и предубеждение и зомби', 5)
        collector.set_book_rating('Что делать, если ваш кот хочет вас убить', 5)

        # проверяем, что длина массива с книгами, имеющими рейтиг 6, равна 0
        assert len(collector.get_books_with_specific_rating(6)) == 0

    def test_get_books_rating_get_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет тип dict
        assert len(collector.get_books_rating()) == 2
        assert type(collector.get_books_rating()) is dict

    def test_add_book_in_favorites_add_none_existing_book(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # добавляем в избранные книгу, которая отсутствует в словаре
        collector.add_book_in_favorites('Униженные и оскорблённые')

        # список favorites, который нам возвращает метод get_list_of_favorites_book, имеет длину 0
        # список favorites, который нам возвращает метод get_list_of_favorites_book, имеет тип list
        assert len(collector.get_list_of_favorites_books()) == 0
        assert type(collector.get_list_of_favorites_books()) is list

    def test_add_book_in_favorites_add_existing_book(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # добавляем в избранные книгу, которая присутствует в словаре
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')

        # список favorites, который нам возвращает метод get_list_of_favorites_book, имеет длину 1
        # список favorites, который нам возвращает метод get_list_of_favorites_book, имеет тип list
        # книга присутствует в списке favorites, который нам возвращает метод get_list_of_favorites_book
        assert len(collector.get_list_of_favorites_books()) == 1
        assert type(collector.get_list_of_favorites_books()) is list
        assert 'Что делать, если ваш кот хочет вас убить' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_delete_book(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # добавляем книгу в избранное
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')

        #удаляем книгу из избранного
        collector.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')

        # список favorites, который нам возвращает метод get_list_of_favorites_book, имеет длину 0
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_get_list_of_favorites_books_get_two_book(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # добавляем книги в избранное
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')

        # список favorites, который нам возвращает метод get_list_of_favorites_book, имеет длину 2
        assert len(collector.get_list_of_favorites_books()) == 2