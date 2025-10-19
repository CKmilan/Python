# This program opens a csv using sys.argv and asks for a name for the output file
# Tn the input file there are names separated with ","-s and the House they are in (Gryffindor etc.)
# The program cleans the names and the houses and gives us a clean csv as output.

import sys
import csv

def main():
    sys_validate()

#READING THE FILE AND ADDING TO A LIST
    try:
        list = []
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                last, first = row["name"].split(", ")
                list.append({"first": first, "last" : last, "house" : row["house"]})
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
#WRITING THE NEW FILE

    with open(sys.argv[2], "w") as newfile:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(newfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in list:
            writer.writerow(row)


#SYS VALIDATION
def sys_validate():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif ".csv" not in sys.argv[1] and ".csv" not in sys.argv[2]:
        sys.exit("Wrong file format")




if __name__ == "__main__":
    main()
