# This program opens a csv using sys.argv, reads its content
# then prints it in the terminal.

from tabulate import tabulate
import sys
import csv

def main():
    try:
        sys_validate()
        list1 = open_file()
        print(tabulate(list1, headers="keys", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")



#Checking the right file format
def sys_validate():

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")



#Opening the file and adding to a list
def open_file():
    with open(sys.argv[1], newline='') as file:
        reader = csv.DictReader(file)
        list1 = []
        for row in reader:
            list1.append(row)
    return list1


if __name__ == "__main__":
    main()