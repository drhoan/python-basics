import hw6_7

def test_hw6_7():
    assert hw6_7.sumEven([1, 2, 3, 4, 5]) == 6
    assert hw6_7.sumEven([1, 2, 3, 4, 5, 6]) == 12
    assert hw6_7.sumEven([1, 2, 3, 4, 5, 6, 7]) == 12
    assert hw6_7.sumEven([2, 4, 6, 8, 10]) == 30
    assert hw6_7.sumEven([1, 3, 5, 7, 9]) == 0

if __name__ == "__main__":
    test_hw6_7()
    print("hw6_7_test.py is done")