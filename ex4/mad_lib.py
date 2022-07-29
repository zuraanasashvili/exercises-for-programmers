def get_input():
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    adverb = input("Enter an adverb: ")
    return noun, verb, adjective, adverb


def create_mad_lib(noun, verb, adjective, adverb):
    print(f"Do you {verb} your {adjective} {noun} {adverb}? That's hilarious")


def main():
    noun, verb, adjective, adverb = get_input()
    create_mad_lib(noun, verb, adjective, adverb)

if __name__ == '__main__':
    main()
