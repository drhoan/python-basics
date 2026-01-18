import hw6_6

def test_hw6_6():
    assert hw6_6.countOdd([1, 2, 3, 4, 5]) == 3
    assert hw6_6.countOdd([1, 2, 3, 4, 5, 6]) == 3
    assert hw6_6.countOdd([1, 2, 3, 4, 5, 6, 7]) == 4
    assert hw6_6.countOdd([2, 4, 6, 8, 10]) == 0
    assert hw6_6.countOdd([1, 3, 5, 7, 9]) == 5

if __name__ == "__main__":
    test_hw6_6()
    print("hw6_6_test.py is done")