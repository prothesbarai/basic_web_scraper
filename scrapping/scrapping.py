class Asp:
    names = "Prothes"

    def __init__(self, age, year):
        self.age = age
        self.year = year
        if self.age > 18:
            self.result = "Adult Person"
        else:
            self.result = "Child"
        self.finalR = f"This is {self.names}. And he is {self.result}"

    def display(self):
        print(self.finalR)
