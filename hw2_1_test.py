import hw2_1

def test_sum_to():
    assert hw2_1.sum_to(10) == 55, 'Failed on 10'
    assert hw2_1.sum_to(100) == 5050, 'Failed on 100'
    assert hw2_1.sum_to(1000) == 500500, 'Failed on 1000'
    print('All tests passed!')

if __name__ == "__main__":
    test_sum_to()