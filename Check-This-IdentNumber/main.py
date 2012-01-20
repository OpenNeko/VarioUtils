"""This programs checksums various account's identification numbers, 
such as credit card numbers, IMEI numbers, National Provider Identifier
numbers in US and Canadian Social Insurance Numbers.
It uses the Luhn algorithm
"""

def main():
    done = False
    while not done:
        try:
            n = int(raw_input("Enter an identification number here and"+
                          "press return: "))
        except ValueError:
            print "Invalid value (not an integer). Retry."
        else:
            done = True

    n = [int(i) for i in str(n)]
    for s in n[::-2]:
        d = sum(n[-1::2], s*2)
    if d%10 == 0:
        print "Valid!"
    else:
        print "Invalid! Check you identification number again."


main()
