import datetime

def get_input():
    age = int(input("What is your current age? "))
    des_age = int(input("At what age would you like to retire? "))
    return age, des_age

def calculate_retirement(age, des_age):
    year = datetime.date.today().year
    print(f"You have {des_age - age} years left until you can retire.")
    print(f"It's {year}, so you can retire in {year + des_age - age}")

def main():
    age, des_age = get_input()
    if age > des_age:
        print("You can already retire")
    else:
        calculate_retirement(age, des_age)


if __name__ == '__main__':
    main()
