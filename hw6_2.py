# Starting with the list in the previous exercise, write Python statements to do the following:
# a. Append “apple” and 76 to the list.
# b. Insert the value “cat” at position 3.
# c. Insert the value 99 at the start of the list.  
# d. Find the index of “hello”.
# e. Count the number of 76s in the list.
# f. Remove the first occurrence of 76 from the list.
# g. Remove True from the list using pop and index.

def main():
    myList = [76, 92.3, "hello", True, 4, 76]
    myList.append("apple") #a
    myList.append(76) #a
    myList.insert(3, "cat") #b
    myList.insert(0, 99) #c
    myList.index("hello")
    myList.count(76) #e
    myList.remove(76) #f
    myList.pop(myList.index(True)) #g

    return myList

if __name__ == "__main__":
    print(main())  # expect [99, 92.3, 'hello', 'cat', 4, 76, 'apple', 76]