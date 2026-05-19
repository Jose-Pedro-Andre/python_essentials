#!/usr/bin/python3

import sys
def great(name, language="en"):
    map_greatings = {"en": "Hello",
                     "pt" : "Olá",
                     "fr" : "Bonjour"}
    try:
        target =  map_greatings[language]
        if target == None:
            return None
        return f"{target}, {name}"
    except:
        return None

def main():
    argc = len(sys.argv)
    if argc != 3:
        print("Wrong arguments")
        sys.exit(1)
    great_result = great(sys.argv[1], sys.argv[2])
    if (great_result == None):
        print("No greatings found")
        return
    print(great_result)

main()