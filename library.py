class Library:
    def __init__(self):
        self.available_book = set()
        self.borrowed_book = set()

    def add_book(self,title):
        all_book= self.available_book | self.borrowed_book
        if not title:
            return "Title is empty."
        if title in all_book:
            return "This book is already added before."
        else:
            self.available_book.add(title)
            return f"The book '{title.title()}' has been added successfully.'"

    def show_available_book(self):
        if not self.available_book:
            return "Available book collection is empty."
        output_line=["Available Book List:"]
        for index,title in enumerate(self.available_book,start=1):
            output_line.append(f"{index}. {title.title()}")
        return "\n".join(output_line)

    def borrow_a_book(self,title):
        if not title:
            return "Book title is empty."
        elif title in self.borrowed_book:
            return f"This book '{title.title()}' is already borrowed."
        elif title not in self.available_book:
            return f"This book '{title.title()}' is not available in library."
        self.available_book.remove(title)
        self.borrowed_book.add(title)
        return f"The book {title.title()} has been borrowed successfully"
    
    def show_borrowed_book(self):
        if not self.borrowed_book:
            return "Borrowed book list is empty."
        output_line=["Borrowed Book List:"]
        for index,title in enumerate(self.borrowed_book,start=1):
            output_line.append(f"{index}. {title.title()}")
        return "\n".join(output_line)

    def return_book(self,title):
        if not title:
            return "Book title is empty."
        elif title not in self.borrowed_book:
            return f"This book '{title.title()}' is invalid."
        self.available_book.add(title)
        self.borrowed_book.remove(title)
        return f"The book {title.title()} has been returned successfully"
    

