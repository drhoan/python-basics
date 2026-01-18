import hw2_3

def test_mean():
    assert hw2_3.mean(1, 2, 3) == 2.0, 'Failed on 1, 2, 3'
    assert hw2_3.mean(10, 20, 30) == 20.0, 'Failed on 10, 20, 30'
    assert hw2_3.mean(100, 200, -300) == 0.0, 'Failed on 100, 200, -300'
    print('All tests passed!')

if __name__ == "__main__":
    test_mean()