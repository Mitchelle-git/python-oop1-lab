#!/usr/bin/env python3

class Coffee:
    def __init__(self, coffee_type, size, price, caffeine_content):
        # Attributes of the Coffee
        self.coffee_type = coffee_type
        self.size = size
        self.price = price
        self.caffeine_content = caffeine_content  # mg
        self.is_brewed = False

    def brew(self):
        """Brew the coffee"""
        self.is_brewed = True
        return f"Brewing a {self.size} {self.coffee_type}."

    def drink(self, amount):
        """Drink coffee and reduce caffeine content"""
        if self.caffeine_content <= 0:
            return "Coffee is finished!"
        self.caffeine_content -= amount
        if self.caffeine_content < 0:
            self.caffeine_content = 0
        return f"Caffeine remaining: {self.caffeine_content}mg"

    def get_info(self):
        """Return formatted coffee info"""
        return f"{self.size} {self.coffee_type} - ${self.price:.2f}, Caffeine: {self.caffeine_content}mg"