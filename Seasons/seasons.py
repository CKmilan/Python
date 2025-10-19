# This program counts the days between the date of birth and today
# then converts it to minutes and convert it to words

import sys
from datetime import date
import operator
import inflect

p = inflect.engine()

def main():
    try:
        print("Date of Birth: 1993-11-3")
        result = difference()
        print(result)

    except (IndexError, ValueError):
        sys.exit("Wrong input")

def difference():
    # Átalakítjuk a sys_argv[1]-et erre a formátumra: 1993, 11, 3
    date_today = date.today()
    date_born = "1993-11-3"
    year, month, day = date_born.split("-")
    date_born = date(int(year), int(month), int(day))

    # Kivonjuk ezt a jelenlegi dátmból
    #date_diff = date_today - date_born

    # Megkapjuk a 2 dátum közötti különbséget napokban
    diff = operator.__sub__(date_today, date_born)
    days = diff.days
    days = int(days)

    # A napokat perccé alakítjuk, majd szavakká
    minutes = days * 24 * 60
    minutes_in_words = p.number_to_words(minutes)
    minutes_in_words = minutes_in_words.capitalize()

    return f"{minutes_in_words} minutes"

if __name__ == "__main__":
    main()
