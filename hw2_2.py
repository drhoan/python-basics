# City Names: Write a function called city_country() that takes in the name of a capital and its country.
# The function should return a string formatted like below if parameter capital is Santiago and parameter country is Chile
# "Santiago is the capital of Chile"
def city_country(capital, country):
    return capital + " is the capital of " + country


if __name__ == "__main__":
    capital = input("Enter a capital: ")
    country = input("Enter a country: ")
    print(city_country(capital, country))