def get_input():
    input_string = input("What is the input string? ")
    return input_string

def count_chars(input):
    ccount = len(input)
    print(f"{input} has {ccount} characters.")

def main():
    input_string = get_input()
    if len(input_string) == 0:
        print("You must enter something")
    else:
        count_chars(input_string)


if __name__ == '__main__':
    main()
