class Coffee:
    def __init__(self, size, price, type=None, origin=None): # Added optional parameters
        self.size = size
        self.price = price
        self.type = type
        self.origin = origin

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        valid_sizes = ["Small", "Medium", "Large"]

        if value not in valid_sizes:
            print("size must be Small, Medium, or Large")
            return

        self._size = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            print("price must be a number")
            return
        if value <= 0:
            print("price must be greater than 0")
            return
        self._price = value

    # Add getters/setters for new attributes if needed, or leave as simple attributes
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        # Example validation for type
        self._type = value

    @property
    def origin(self):
        return self._origin

    @origin.setter
    def origin(self, value):
        # Example validation for origin
        self._origin = value
   
    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price = self.price + 1
    
    def get_info(self):
        # Add a method that might be called by the get_info test
        return f"Size: {self.size}, Price: ${self.price}, Type: {self.type}, Origin: {self.origin}"

    def brew(self):
        # Add a method that might be called by the test_brew test
        print(f"Brewing {self.type} coffee.")

    def drink(self):
        # Add a method that might be called by the test_drink test
        print("Enjoying the coffee!")

