from functools import reduce

class OneLinerChag:
    def __init__(self) -> None:
        pass

    def chag1(self):
        print("chag1", end=" -> ")
        res = [i**2 for i in range(1,11) if i%2==0]
        print(res)

    def chag2(self):
        print("chag2", end=" -> ")
        res = [word.upper() for word in ["Hello", "World"]]
        print(res)

    def chag3(self):
        print("chag3", end=" -> ")
        res = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5], 10)
        print(res)

if __name__ == "__main__":
    oneLinerChag = OneLinerChag()
    oneLinerChag.chag1()
    oneLinerChag.chag2()
    oneLinerChag.chag3()