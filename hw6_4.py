# Write a Python function named findmax(lst) that takes a parameter  containing
# a nonempty list of integers and returns the maximum value.
# (Note: there is a builtin function named max but pretend you cannot use it)

def findmax(lst):
    # Replace the pass statement with your code
    pass

if __name__ == "__main__":
    # Home-built findmax function
    print(findmax([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # 10
    print(findmax([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))  # 10
    print(findmax([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))  # 10
    # Built-in max function
    print(max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))  # 10