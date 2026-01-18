import hw6_3

def test_hw6_3():
    assert hw6_3.average([1, 2, 3, 4, 5]) == 3.0
    assert hw6_3.average([1, 2, 3, 4, 5, 6]) == 3.5
    assert hw6_3.average([1, 2, 3, 4, 5, 6, 7]) == 4.0

if __name__ == "__main__":
    test_hw6_3()
    print("hw6_3_test.py is done")