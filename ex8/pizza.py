PIZZA_SLICES = 8

def get_input():
    people = int(input("How many people? "))
    pizzas = int(input("How many pizzas do you have? "))
    return people, pizzas

# This calculation does not work
def calc_pizzas(people, pizzas):
    print(f"{people} with {pizzas} pizzas")
    print(f"Each person gets {pizzas * PIZZA_SLICES / people}")



def main():
    people, pizzas = get_input()
    calc_pizzas(people, pizzas)

if __name__ == '__main__':
    main()
