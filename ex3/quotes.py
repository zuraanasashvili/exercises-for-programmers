def get_input():
    input_quote = input("What is the quote? ")
    input_author = input("Who said it? ")
    return input_quote, input_author

def create_quote(quote, author):
    print(f"{author} says, \"{quote}\"")


def main():
    quote, author = get_input()
    create_quote(quote, author)

if __name__ == '__main__':
    main()
