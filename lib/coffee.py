# Coffee class representing a coffee item in the bookstore

class Coffee:

    def __init__(self, size, price):
        # Set the size and price when a Coffee is created
        self.size = size
        self.price = price

    @property
    def size(self):
        # Return the size value
        return self._size

    @size.setter
    def size(self, value):
        # Only allow Small, Medium, or Large for size
        if value not in ["Small", "Medium", "Large"]:
            print("size must be Small, Medium, or Large")
        else:
            self._size = value

    def tip(self):
        # Print a thank you message and increase the price by 1
        print("This coffee is great, here’s a tip!")
        self.price += 1