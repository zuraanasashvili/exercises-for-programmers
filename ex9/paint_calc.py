GALLON_FEET = 350

def get_input():
    length = int(input("What is the length? "))
    width = int(input("What is the width? "))
    return length, width

def calc_paint(length, width):
    square_feet = length * width
    if square_feet % GALLON_FEET > 0:
        gallons = square_feet // GALLON_FEET + 1
    else:
        gallons = square_feet / GALLON_FEET
    print(f"You will need to purchase {gallons} of paint to cover {square_feet} square feet.")


def main():
    length, width = get_input()
    calc_paint(length, width)

if __name__ == '__main__':
    main()
