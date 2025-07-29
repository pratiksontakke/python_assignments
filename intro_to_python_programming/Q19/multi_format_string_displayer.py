class MultiFormattedStr:
    def __init__(self):
        self.name = "Pratik"
        self.age = "28"
        self.city = "Nagpur"
        
    def using_percent_formatting(self):
         print("My name is %s, I am %s year old, and I live in %s"%(self.name, self.age, self.city))

    def using_format(self):
        print("My name is {}, I am {} year old, and I live in {}".format(self.name, self.age, self.city))

    def using_f_string(self):
        print(f"My name is {self.name}, I am {self.age} year old, and I live in {self.city}")

if __name__ == "__main__":
    multiFormattedStr = MultiFormattedStr()
    multiFormattedStr.using_percent_formatting()
    multiFormattedStr.using_format()
    multiFormattedStr.using_f_string()