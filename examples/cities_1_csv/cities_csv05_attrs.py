import csv
import attr


@attr.s(auto_attribs=True, frozen=True)
class City:
    name: str
    lat: float
    lng: float
    country: str


def main():
    with open("../data/worldcities.csv") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            if row['country'] != "Israel":
                continue

            city = City(
                name=row['city_ascii'],
                lat=float(row['lat']),
                lng=float(row['lng']),
                country=row['country'],
            )

            print(city)


if __name__ == '__main__':
    main()
