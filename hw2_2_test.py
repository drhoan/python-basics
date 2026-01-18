import hw2_2

def test_city_country():
    assert hw2_2.city_country('Santiago', 'Chile') == 'Santiago is the capital of Chile', 'Failed on Santiago, Chile'
    assert hw2_2.city_country('London', 'England') == 'London is the capital of England', 'Failed on London, England'
    assert hw2_2.city_country('Paris', 'France') == 'Paris is the capital of France', 'Failed on Paris, France'
    print('All tests passed!')

if __name__ == "__main__":
    test_city_country()