import csv


def main():
    with open("../data/worldcities.csv") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            if row['country'] != "Israel":
                continue

            print(dict(row))


if __name__ == '__main__':
    main()
