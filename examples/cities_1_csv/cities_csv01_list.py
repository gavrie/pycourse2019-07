import csv


def main():
    with open("../data/worldcities.csv") as csv_file:
        reader = csv.reader(csv_file)

        for row in reader:
            country = row[4]
            if country != "Israel":
                continue

            print(row)


if __name__ == '__main__':
    main()
