def get_name():
    name = input("what is your name? ")
    return name

def greet(name):
    print(f"Hello, {name}, nice to meet you!")

def main():
    name = get_name()
    greet(name)


if __name__ == '__main__':
    main()
