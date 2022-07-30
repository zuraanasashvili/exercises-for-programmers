FEET_CONSTANT = 0.09290304

def get_input():
    length = int(input("What is the length of the room in feet? "))
    width = int(input("What is the width of the room in feet? "))
    return length, width

def calculate_area(length, width):
    area = length * width
    doublef_const = round(area * FEET_CONSTANT, 3)
    print(f"You entered dimensions of {length} feet by {width} feet.")
    print("The area is")
    print(f"{length * width} square feet")
    print(f"{doublef_const} square meters")

def main():
    length, width = get_input()
    calculate_area(length, width)

if __name__ == '__main__':
    main()
