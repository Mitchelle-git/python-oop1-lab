#!/usr/bin/env python3
#!/usr/bin/env python3

class Coffee:
    VALID_SIZES = ["Small", "Medium", "Large"]

    def __init__(self, coffee_type="", size="Medium", price=0.0, caffeine_content=0):
        # Attributes
        self.coffee_type = coffee_type
        self.size = size if size in self.VALID_SIZES else "Medium"
        self.price = price
        self.caffeine_content = caffeine_content
        self.is_brewed = False
        self.tip = 0.0  # For tipping functionality

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

    def add_tip(self, amount):
        """Add tip to coffee price"""
        if amount > 0:
            self.tip += amount
            self.price += amount
        return self.tip

    def get_info(self):
        """Return coffee info"""
        return f"{self.size} {self.coffee_type} - ${self.price:.2f}, Caffeine: {self.caffeine_content}mg"