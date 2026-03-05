class Coffee:
    VALID_SIZES = ["Small", "Medium", "Large"]

    def __init__(self, coffee_type="", size="Medium", price=0.0, caffeine_content=0):
        self.coffee_type = coffee_type
        self.price = price
        self.caffeine_content = caffeine_content
        self.is_brewed = False
        self._tip = 0.0  # make tip private for method access

        # Validate size
        if size not in self.VALID_SIZES:
            self.size_error = "size must be Small, Medium, or Large\n"
            self.size = "Medium"
        else:
            self.size_error = ""
            self.size = size

    def tip(self, amount):
        """Add tip to coffee price"""
        if amount > 0:
            self._tip += amount
            self.price += amount
        return self._tip

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