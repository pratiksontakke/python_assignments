# Higher-Order Function Implementations

# Custom map function
def custom_map(func, iterable):
    return [func(x) for x in iterable]

# Custom filter function
def custom_filter(func, iterable):
    return [x for x in iterable if func(x)]

# Custom reduce function
def custom_reduce(func, iterable):
    result = iterable[0]
    for x in iterable[1:]:
        result = func(result, x)
    return result


# -------------------------------
# Example Usage
# -------------------------------

if __name__ == "__main__":
    numbers = [1, 2, 3, 4]

    # Multiply each element by 2
    mapped = custom_map(lambda x: x * 2, numbers)
    print("custom_map result:", mapped)         # ➞ [2, 4, 6, 8]

    # Filter even numbers
    filtered = custom_filter(lambda x: x % 2 == 0, numbers)
    print("custom_filter result:", filtered)    # ➞ [2, 4]

    # Reduce: sum of all elements
    reduced = custom_reduce(lambda x, y: x + y, numbers)
    print("custom_reduce result:", reduced)     # ➞ 10
