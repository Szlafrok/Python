from pokazowe import *

class BrowserHistory():
    def __init__(self):
        self.history = Stack()
        self.current_page = None

    def go_to_page(self, url):
        self.history.push(self.current_page)
        self.current_page = url

    def go_back(self):
        previous_page = self.history.pop()
        if previous_page != None:
            self.current_page = previous_page

    def print_history(self):
        print(f"Aktualna strona: {self.current_page}")
        print("History:")
        for page in reversed(self.history.stack):
            print(page)

history = BrowserHistory()
history.go_to_page("YouTube")
history.go_to_page("Giganci")
history.go_to_page("Ziemniak")
history.go_to_page("Memy o papieżu")
history.print_history()
history.go_back()
history.print_history()
