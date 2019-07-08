import csv


class City:
    def __init__(self, name, lat, lng, country):
        self.name = name
        self.lat = lat
        self.lng = lng
        self.country = country

    def __repr__(self):
        return f"City(name={self.name!r}, lat={self.lat}, lng={self.lng}, country={self.country!r})"

    def __eq__(self, other):
        return (self.name == other.name and
                self.lat == other.lat and
                self.lng == other.lng and
                self.country == other.country)


def main():
    with open("../data/worldcities.csv") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            city = City(
                name=row['city_ascii'],
                lat=float(row['lat']),
                lng=float(row['lng']),
                country=row['country'],
            )

            if city.country != "Israel":
                continue

            print(city)


if __name__ == '__main__':
    main()
