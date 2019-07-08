def get_fields(line):
    fields_quoted = line.strip().split(",")
    fields = [f.strip('"') for f in fields_quoted]
    return fields


def get_cities(filename):
    csv_file = open(filename)
    _header = next(csv_file)

    cities = []

    for line in csv_file:
        city = get_fields(line)
        cities.append(city)

    return cities


def get_cities_in_country(cities, country):
    """
    Returns the cities from the provided list that are in the specified country.
    """
    raise NotImplementedError


def get_cities_above_latitude(cities, lat):
    """
    Returns the cities that are above the specified latitude
    """
    raise NotImplementedError


def test_cities_in_israel():
    cities = get_cities("../data/worldcities.csv")
    matching_cities = get_cities_in_country(cities, "Israel")
    names = [city[0] for city in matching_cities]
    assert names == ['Jerusalem', 'Beer Sheva', 'Nazareth', 'Tel Aviv-Yafo', 'Haifa', 'Ramla']


def test_cities_above_latitude_80():
    cities = get_cities("../data/worldcities.csv")
    matching_cities = get_cities_above_latitude(cities, 80.0)
    names = [city[0] for city in matching_cities]
    assert names == ['Alert', 'Nord']
