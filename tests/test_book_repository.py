from lib.book_repository import BookRepository
from lib.book import Book

def test_get_all_books(db_connection):
    db_connection.seed("seeds/book_store.sql")
    book_repo = BookRepository(db_connection)

    books = book_repo.all()

    assert books[0] == Book(1, 'Nineteen Eighty-Four', 'George Orwell')
    assert books[-1] == Book(5, 'The Age of Innocence', 'Edith Wharton')