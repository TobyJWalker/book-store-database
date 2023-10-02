from lib.book import Book

def test_book_initialise():
    book = Book(1, 'test title', 'test author')

    assert book.id == 1
    assert book.title == 'test title'
    assert book.author_name == 'test author'

def test_book_repr():
    book = Book(1, 'test title', 'test author')

    assert str(book) == 'Book(1, test title, test author)'

def test_book_eq():
    book1 = Book(1, 'test title', 'test author')
    book2 = Book(1, 'test title', 'test author')

    assert book1 == book2