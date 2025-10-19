# This program asks for a credit card number and checks its validation using the Luhn's Algorithm.
# If it is valid it gives the card's type as outout.

def main():
    try:
        card = int(input("Number: "))
        card_validation = isvalid(card)
    except ValueError:
        print("INVALID")

    if card_validation == True:
        print(card_type(card))
    else:
        print("INVALID")



def isvalid(card):
    card_og = card
    strsum = ""
    intsum = 0

    # Every other num multiplied by 2
    card = card / 10
    card = int(card)
    while card > 0:
        strsum += str((int(card) % 10) * 2)
        card = int(card) / 100

    # Sum the digits of the strsum
    for i in strsum:
        intsum += int(i)

    # Every num left
    sum = 0
    while card_og > 0:
        sum += (int(card_og) % 10)
        card_og = int(card_og) / 100

    # Solution
    solution = sum + intsum
    if solution % 10 == 0:
        return True
    else:
        return False


def card_type(card):
    card = str(card)
    if len(card) == 15 and card[:2] == "34" or card[:2] == "37":
        return "AMEX"
    if len(card) == 13 or len(card) == 16 and card[0] == "4":
        return "VISA"
    if len(card) == 16 and card[:2] == "51" or card[:2] == "52" or card[:2] == "53" or card[:2] == "54" or card[:2] == "55":
        return "MASTERCARD"
    else:
        return "INVALID"





if __name__ == "__main__":
    main()
