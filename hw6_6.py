# Write a function countOdd(lst) that takes a list of integers as a parameter
# and returns the number of odd numbers in the list.

def countOdd(lst):
    # Replace the pass statement with your code
    odds = 0
    for i in range(len(lst)):
        if(lst[i] % 2 == 1):
            odds = odds + 1
    return odds
if __name__ == "__main__":
    print(countOdd([1, 2, 3, 4, 5]))  # 3
    print(countOdd([2, 4, 6, 8, 10]))  # 0
    print(countOdd([1, 3, 5, 7, 9]))  # 5