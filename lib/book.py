class Book:
    def __init__(self, title="", author="", page_count=0, price=0.0, genre=""):
        self.title = title
        self.author = author
        self.price = price
        self.genre = genre
        self.current_page = 1

        # Validate page_count
        if not isinstance(page_count, int):
            self.page_count_error = "page_count must be an integer\n"
            self.page_count = 0
        else:
            self.page_count_error = ""
            self.page_count = page_count

    def turn_page(self):
        """Flip a page"""
        if self.current_page < self.page_count:
            self.current_page += 1
        return "Flipping the page...wow, you read fast!"

    def bookmark_page(self, page_number):
        if 1 <= page_number <= self.page_count:
            self.current_page = page_number
        return self.current_page

    def get_info(self):
        return f"'{self.title}' by {self.author}, Genre: {self.genre}, Pages: {self.page_count}, Price: ${self.price:.2f}"