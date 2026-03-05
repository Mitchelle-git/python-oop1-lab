#!/usr/bin/env python3
class Book:
    def __init__(self, title="", author="", pages=0, price=0.0, genre=""):
        # Provide default values so tests can instantiate without full args
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.genre = genre
        self.current_page = 1

    def read_page(self):
        if self.current_page < self.pages:
            self.current_page += 1
        return self.current_page

    def bookmark_page(self, page_number):
        if 1 <= page_number <= self.pages:
            self.current_page = page_number
        return self.current_page

    def get_info(self):
        return f"'{self.title}' by {self.author}, Genre: {self.genre}, Pages: {self.pages}, Price: ${self.price:.2f}"