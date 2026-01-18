import hw2_4

def test_fuel_cost():
    assert hw2_4.fuel_cost(100, 25, 3.50) == 14.0, 'Failed on 100, 25, 3.50'
    assert hw2_4.fuel_cost(200, 25, 3.50) == 28.0, 'Failed on 200, 25, 3.50'
    assert hw2_4.fuel_cost(200, 35, 3.50) == 20.0, 'Failed on 200, 35, 3.50'
    print('All tests passed!')

if __name__ == "__main__":
    test_fuel_cost()