class IOstring():
    def __init__(self):
        self.str=" "
    def get_string(self):
        self.str=input("Enter the string: ")
    def print_string(self):
        print("The result is: ",self.str.upper())

str=IOstring()
str.get_string()
str.print_string()
