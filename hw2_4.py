# Write a function called fuel_cost that takes a distance, mpg, and cost of one gallon of gas as arguments.
# The function should return the fuel cost to drive the distance in dollars.
# For example, fuel_cost(100, 25, 3.50) should return 14.0.
def fuel_cost(distance, mpg, cost):
    pass # replace this line with your code


if __name__ == "__main__":
    distance = float(input("Enter a distance: "))
    mpg = float(input("Enter a mpg: "))
    cost = float(input("Enter a cost: "))
    print(f'The fuel cost to drive {distance} miles is ${fuel_cost(distance, mpg, cost)}')
