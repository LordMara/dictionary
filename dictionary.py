#!/usr/bin/env python3
import csv


def is_number(s):       # check if command is only integer
    try:
        int(s)
        return True
    except ValueError:
        pass


def search(a):
    explanation = []
    appellation = []
    source = []

    with open("dictionary.csv", "r") as f:      # open file, read row and add items to list of same name
        d = csv.DictReader(f)
        for row in d:
            appellation.append(row["appellation"])
            explanation.append(row["explanation"])
            source.append(row["source"])

    z = []
    for c in zip(explanation, source):      # make tuple with this items
        z.append(c)

    my_dictionary = {}
    for i in range(len(appellation)):       # make dictionary, set items from lis appellation
        appellation[i] = appellation[i].lower()     # as key and tuple as definition
        my_dictionary[appellation[i]] = z[i]
    global test     # check if key is in file
    test = 0        # value to break while loop for check if key is in file
    try:
        a in appellation
        return my_dictionary[a]
    except KeyError:
        test = 1        # valou to run while loop
        return "Wrong appeltation. Input new one: "


def sort():
    appellation = []
    with open("dictionary.csv", "r") as f:
        d = csv.DictReader(f)
        for row in d:
            appellation.append(row["appellation"])      # all keys to list
    z = sorted(appellation, key=str.lower)     # here is sorted, key to sort independly
    return z        # from lower/upper case


def same_key(a):        # check if inserted key in command 2 is alredy in keychain
    appellation = []
    with open("dictionary.csv", "r") as f:
        d = csv.DictReader(f)
        for row in d:
            appellation.append(row["appellation"])
        if a in appellation:
            return True


def write(a, b, c):     # write new key definition and source to file
    with open("dictionary.csv", "a") as csvfile:        # open file to add to last position
        fieldnames = ["appellation", "explanation", "source"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writerow({"appellation": a, "explanation": b, "source": c})
    return


def show(a):
    explanation = []
    appellation = []
    source = []

    with open("dictionary.csv", "r") as f:      # open file, read row and add items to list of same name
        d = csv.DictReader(f)
        for row in d:
            appellation.append(row["appellation"])
            explanation.append(row["explanation"])
            source.append(row["source"])

    z = []
    for c in zip(explanation, source):      # make tuple with this items
        z.append(c)

    my_dictionary = {}
    for i in range(len(appellation)):       # make dictionary, set items from lis appellation
        appellation[i] = appellation[i].lower()     # as key and tuple as definition
        my_dictionary[appellation[i]] = z[i]

    new = []
    to_print = []

    for x in range(0, len(appellation)):
        if a in appellation[x][0]:  # check is letter in any appeltion
            new.append(appellation[x])  # add al matched appeltions to new list

    for z in range(0, len(new)):
        v = [new[z], my_dictionary[new[z]]]     # with all apellations in new list us them
        to_print.append(v)      # to dictionay outuput and put all of them to new list

    global test2    # for chek if is letter and in any appellation
    test2 = 0
    if len(to_print) == 0 or a == "":      # is input was now match we have list without elements
        test2 = 1       # so we run next while loop
        return ""
    else:
        return to_print


while True:     # if 0 not given will remain
    print("""Dictionary for a little programmer:
    1) search explanation by appellation
    2) add new definition
    3) show all appellations alphabetically
    4) show available definitions by first letter of appellation
    0) exit""")

    command = input("Enter number of command: ")       # input command to menu
    if is_number(command):          # is command corresct
        command = int(command)
        if command > - 1 and command < 5:

            if command == 1:
                test = 1
                while test == 1:        # check if given key is in file
                    print("What is you appelation? ")
                    question = input().lower()
                    k = search(question)
                    print(question, ",", k, '\n')

            elif command == 2:
                app = input("Input new appeltation: ")      # is key to new definition corresct
                while app is "" or app.isspace() or same_key(app):
                    app = input("Invalid input. Input new appeltation: ")
                exp = input("Input new explenation: ")
                sou = input("Input new source: ")
                write(app, exp, sou)
                print("")

            elif command == 3:
                x = sort()
                print("Appelations in alphabetic order: ", ", ".join(x), '\n')

            elif command == 4:
                show_on = input("Input first letter of searching word: ")
                test2 = 1
                h = show(show_on)
                while test2 == 1:        # try is letter and is in any key or enter was input
                    print("No such input. Try different one")
                    show_on = input()
                    h = show(show_on)
                for g in range(len(h)):
                    print(h[g][0], ",", h[g][1], '\n')

            elif command == 0:
                break
        else:
            print("Wrong command. Input new one", '\n')
    else:
        print("Wrong command. Input new one", '\n')
