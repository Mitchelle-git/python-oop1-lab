#!/usr/bin/env python3
class Coffee:
    def __init__(self, coffee_type="", size="", price=0.0, caffeine_content=0):
        # Default values to satisfy tests
        self.coffee_type = coffee_type
        self.size = size
        self.price = price
        self.caffeine_content = caffeine_content
        self.is_brewed = False

    def brew(self):
        self.is_brewed = True
        return f"Brewing a {self.size} {self.coffee_type}."

    def drink(self, amount):
        if self.caffeine_content <= 0:
            return "Coffee is finished!"
        self.caffeine_content -= amount
        if self.caffeine_content < 0:
            self.caffeine_content = 0
        return f"Caffeine remaining: {self.caffeine_content}mg"

    def get_info(self):
        return f"{self.size} {self.coffee_type} - ${self.price:.2f}, Caffeine: {self.caffeine_content}mg"