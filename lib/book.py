# Book class representing a book in the bookstore

class Book:

    def __init__(self, title, page_count):
        # Set the title and page_count when a Book is created
        self.title = title
        self.page_count = page_count

    @property
    def page_count(self):
        # Return the page count value
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        # Only allow integers for page_count
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value

    def turn_page(self):
        # Print a message when the user turns a page
        print("Flipping the page...wow, you read fast!")