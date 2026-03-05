#!/usr/bin/env python3
#!/usr/bin/env python3

class Book:
    def __init__(self, title="", author="", page_count=0, price=0.0, genre=""):
        # Attributes
        self.title = title
        self.author = author
        self.page_count = page_count if isinstance(page_count, int) else 0
        self.price = price
        self.genre = genre
        self.current_page = 1

    def turn_page(self):
        """Move to the next page"""
        if self.current_page < self.page_count:
            self.current_page += 1
        return self.current_page

    def bookmark_page(self, page_number):
        """Bookmark a specific page"""
        if 1 <= page_number <= self.page_count:
            self.current_page = page_number
        return self.current_page

    def get_info(self):
        """Return book info"""
        return f"'{self.title}' by {self.author}, Genre: {self.genre}, Pages: {self.page_count}, Price: ${self.price:.2f}"