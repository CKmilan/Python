# This program gives you math problems to solve

import random

def main():
    generate_integer(get_level())

def get_level():
    try:
        while True:

            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                return level

    except ValueError:
        level = int(input("Level: "))
        return level


def generate_integer(level):
    tries = 0
    score = 0
    for i in range(1, 11):
        if level == 1:
            x = random.randint(0, 9)
            y = random.randint(0, 9)

        elif level == 2:
            x = random.randint(10, 99)
            y = random.randint(10, 99)

        elif level == 3:
            x = random.randint(100, 999)
            y = random.randint(100, 999)

        sum = x + y
        answer = int(input(f"{x} + {y} = "))
        if sum == answer:
            tries = 0
            score += 1
            continue

        if sum != answer:
            while tries < 2 and sum != answer:
                tries += 1
                print("EEE")
                answer = int(input(f"{x} + {y} = "))

            if sum != answer and tries == 2:
                print(f"{x} + {y} = {x + y}")

    print(f"Score: {score}")


if __name__ == "__main__":
    main()