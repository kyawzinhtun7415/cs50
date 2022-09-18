# CS50's Introduction to Programming with Python
# Final Project
# Student Management System
# I am Kyaw Zin Tun @ Wong Wun Kwint
# I am from Taipei, Taiwan

import csv
import sys
import pandas as pd


def main():
    while True:
        check_sys()
        try:
            print(
                """
        Welcome to My CS50P Project!
        Choose command 1 to 4:
        1. Display CSV data
        2. Search data
        3. Display and Save CSV file with Letter Grade
        4. Exit
    """
            )
            choice = int(input("Please enter 1 to 4: "))
            print()
        except ValueError:
            print()
            print("Please choose from only number 1 to 4")
        else:
            option(choice)


def check_sys():
    """
    check number of command-line arguments and if there is a csv file
    """
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1]:
        sys.exit("Please enter csv file")


def option(choice):
    """
    compute each function of choice chosen

    :param choice: number of choice to perform
    :type choice: int
    """

    match choice:
        case 1:
            display()
        case 2:
            search_grade()
        case 3:
            letter_grade()
        case 4:
            print("Thank you")
            sys.exit()


def display():
    """
    display the csv file in table
    """
    try:
        df = pd.read_csv(sys.argv[1])
        df2 = df.to_string(index=False)
        print(df2)
    except FileNotFoundError:
        sys.exit("Couldn't read CSV file")


def search_grade():
    """
    display the grade of the searched student
    """
    student = input("Enter student name to search for: ")
    print()

    # read the csv file
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            found = False
            for row in reader:
                # if student name is found
                if student == row["name"]:
                    print(
                        f"RollNo.{row['no']} {row['name']}\nGrade: {row['grade']}")
                    found = True
            # if student name is not found
            if found == False:
                print("Not Found")
    except FileNotFoundError:
        sys.exit("Couldn't read CSV file")


def letter_grade():
    """
    print and save the new csv file with letter grades included.
    """

    # transform the csv file to list with individual items in dictionary form
    data = []
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        sys.exit("Couldn't read CSV file")

    # new list with letter grades included in each item
    output = []
    for row in data:
        # marks to letter grade
        letter = a_to_f(row["grade"])
        output.append(
            {
                "no": row["no"],
                "name": row["name"],
                "grade": row["grade"],
                "letter": letter,
            }
        )

    # display the list in table form
    df = pd.DataFrame(output)
    df2 = df.to_string(index=False)
    print(df2)
    # write the list to new csv file
    with open(f"{sys.argv[1]}_new", "w") as file:
        writer = csv.DictWriter(
            file, fieldnames=["no", "name", "grade", "letter"])
        writer.writerow(
            {"no": "no", "name": "name", "grade": "grade", "letter": "letter"}
        )
        for row in output:
            writer.writerow(
                {
                    "no": row["no"],
                    "name": row["name"],
                    "grade": row["grade"],
                    "letter": row["letter"],
                }
            )


def a_to_f(grade) -> int:
    """
    return letter grades corresponding to marks.

    :para grade: number of marks
    :type grade: str
    :return: a letter according to grade
    :rtype: str
    """
    grade = int(grade)
    if 90 < grade <= 100:
        return "A"
    elif 80 < grade <= 90:
        return "B"
    elif 70 < grade <= 80:
        return "C"
    elif 60 < grade <= 70:
        return "E"
    elif 50 < grade <= 60:
        return "F"
    else:
        return "Fail"


if __name__ == "__main__":
    main()
