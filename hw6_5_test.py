import hw6_5

def test_hw6_5():
    assert hw6_5.sum_of_squares([2, 3, 4]) == 29
    assert hw6_5.sum_of_squares([1, 2, 3, 4, 5]) == 55
    assert hw6_5.sum_of_squares([1, 2, 3, 4, 5, 6]) == 91

if __name__ == "__main__":
    test_hw6_5()
    print("hw6_5_test.py is done")