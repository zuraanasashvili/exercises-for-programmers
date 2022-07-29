def get_input():
    first = int(input("What is the first number? "))
    second = int(input("What is the second number? "))
    return first, second

def create_computations(first, second):
    sum_ = first + second
    minus_ = first - second
    multiply_ = first * second
    divide_ = first / second
    print(f"{first} + {second} = {sum_}")
    print(f"{first} - {second} = {minus_}")
    print(f"{first} * {second} = {multiply_}")
    print(f"{first} / {second} = {divide_}")

def main():
    first, second = get_input()
    if first < 0 or second < 0:
        print(first)
        print(second)
        print("Only positive values are allowed")
    else:
        create_computations(first, second)

if __name__ == '__main__':
    main()
