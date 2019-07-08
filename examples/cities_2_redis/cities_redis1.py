import csv
from dataclasses import dataclass

import redis


@dataclass(frozen=True)
class City:
    name: str
    lat: float
    lng: float
    country: str


def main():
    conn = redis.Redis()
    cities_key = "cities"

    with open("../data/worldcities.csv") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            # if row['country'] != "Israel":
            #     continue

            city = City(
                name=row['city_ascii'],
                lat=float(row['lat']),
                lng=float(row['lng']),
                country=row['country'],
            )

            conn.geoadd(cities_key, city.lng, city.lat, city.name)

    # Some examples

    dist = conn.geodist(cities_key, "Tel Aviv-Yafo", "Tarsus", unit="km")
    print(f"Tel Aviv-Yafo <-> Tarsus: {dist} km")

    dist = conn.geodist(cities_key, "Jerusalem", "Haifa", unit="km")
    print(f"Jerusalem <-> Haifa: {dist} km")

    z = conn.georadiusbymember(cities_key, "Jerusalem", unit="km", withdist=True, sort="ASC", radius=600.0)
    print({city: dist for city, dist in z})


if __name__ == '__main__':
    main()
