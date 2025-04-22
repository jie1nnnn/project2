class book():
    def __init__(self):
        self.name = "xiaohan"
        self.title = "x"

    
    def Add(self):
        self.title = input("what book would you like to read.")
        print("you have added", self.title)