import hw6_4

def test_hw6_4():
    assert hw6_4.findmax([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert hw6_4.findmax([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
    assert hw6_4.findmax([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
    assert hw6_4.findmax([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == 10
    assert hw6_4.findmax([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 100, 10]) == 100

if __name__ == "__main__":
    test_hw6_4()
    print("hw6_4_test.py is done")