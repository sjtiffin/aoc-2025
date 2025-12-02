import csv

def check_doubles():


def main():
    with open("input.csv", newline="", encoding="utf-8") as f:
        for ids in csv.reader(f):
            for id in ids:
                first, last = id.split("-")
                range = range(int(first), (int(last) + 1), 1)
                for number in range:



if __name__ == "__main__":
    main()
