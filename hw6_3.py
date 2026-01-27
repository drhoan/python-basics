# Write a function called average that takes a list of numbers as a parameter
# and returns the average of the numbers in the list.

def average(numlist):
    # Replace the pass statement with your code
    average = 0
    for i in range(len(numlist)):
        average = average + numlist[i]
    return average / len(numlist)

if __name__ == "__main__":
    print(average([1, 2, 3, 4, 5, 6, 7]))  # 3.0