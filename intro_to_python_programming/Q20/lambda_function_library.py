from functools import reduce
import math


class LearningLambdaFunc:
    def __init__(self) -> None:
        self.lst = [1,2,3,4,5]

    def square(self):
        res = list(map(lambda x:x**2, self.lst))
        print(f"square : {res}")

    def factorial(self):
        res = list(map(math.factorial, self.lst))
        print(f"factorial : {res}")

    def reverse(self):
        res = list(reversed(self.lst))
        print(f"reverse : {res}")

    def uppercase(self):
        res = list(map(lambda x: x.upper(), ["Pratik", "Sontakke"]))
        print(f"uppercase : {res}")

    def filter_evens(self):
        res = list(map(lambda x:x%2==0, self.lst))
        print(f"filter_evens : {res}")

    def sum_of_list(self):
        res = reduce(lambda x,y:x+y, self.lst)
        print(f"sum_of_list : {res}")


if __name__ == "__main__":
    learningLambdaFunc = LearningLambdaFunc()
    learningLambdaFunc.square()
    learningLambdaFunc.factorial()
    learningLambdaFunc.reverse()
    learningLambdaFunc.uppercase()
    learningLambdaFunc.filter_evens()
    learningLambdaFunc.sum_of_list()