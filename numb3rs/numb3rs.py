# This program checks if the IP is valid using regular expressions.


import re


def main():

    print(validate(input("IPv4 Address: ")))



def validate(ip):

    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        split_ip = ip.split(".")
        for i in split_ip:
            i = int(i)
            if i > 255:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()
