class ComprehensionConverter:
    # [expression for item in iterable if condition]

    def __init__(self) -> None:
        pass

    def normal_for_loop(self):
        print("normal_for_loop", end=" -> ")
        for i in range(10):
            print(f"i : {i}", end=" | ")
        print()

    def conprehension_square(self):
        print("conprehension_square", end=" -> ")
        res =  [i**2 for i in range(10)]
        print(res)

    def conprehension_even(self):
        print("conprehension_even", end=" -> ")
        res = [i for i in range(10) if i%2==0]
        print(res)

    def conprehension_pair(self):
        print("conprehension_pair", end=" -> ")
        res = [(x, y) for x in range(3) for y in range(2)]
        print(res)



if __name__ == "__main__":
    comprehensionConverter = ComprehensionConverter();
    comprehensionConverter.normal_for_loop()
    comprehensionConverter.conprehension_square()
    comprehensionConverter.conprehension_even()
    comprehensionConverter.conprehension_pair()
