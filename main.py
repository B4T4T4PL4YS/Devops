def multiply(a, b):
    return a * b


def is_equal(left, right):
    return left == right


def build_multiplication_message(a, b, result):
    return f"{a} * {b} is equal to {result}"


def run():
    value = multiply(5, 5)
    if is_equal(value, 25):
        print(build_multiplication_message(5, 5, value))


if __name__ == "__main__":
    run()