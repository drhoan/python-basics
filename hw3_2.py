# Write a program that uses a for loop to print "One of the months of the year is January"
# "One of the months of the year is February" "One of the months of the year is March" etc …. 
# Hint you will need to create a list of months before you loop.
# To create a list, use: months = ["January","February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
def print_months():
    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    # TODO: Write a for loop to print "One of the months of the year is January" "One of the months of the year is February" "One of the months of the year is March" etc ….
    for i in range(len(months)):
        months[i] = "One of the months of the year is " + months[i]
        print(months[i])
if __name__ == "__main__":
    print_months()