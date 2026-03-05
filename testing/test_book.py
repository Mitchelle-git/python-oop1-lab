import pytest
from lib.book import Book

def test_book_creation():
    b = Book("1984", "George Orwell", 328, 9.99, "Dystopian")
    assert b.title == "1984"
    assert b.author == "George Orwell"
    assert b.pages == 328
    assert b.current_page == 1

def test_read_page():
    b = Book("1984", "George Orwell", 328, 9.99, "Dystopian")
    b.read_page()
    assert b.current_page == 2

def test_bookmark_page():
    b = Book("1984", "George Orwell", 328, 9.99, "Dystopian")
    b.bookmark_page(100)
    assert b.current_page == 100

def test_get_info():
    b = Book("1984", "George Orwell", 328, 9.99, "Dystopian")
    info = b.get_info()
    assert "1984" in info
    assert "George Orwell" in info