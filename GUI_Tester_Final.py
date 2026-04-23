# -*- coding: utf-8 -*-
import csv
import os

filename = "Garrick.csv"

# Step 0: Always reset CSV to 0 at the very beginning of the script
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([0, 0, 0])

# Step 1: Flag to track first run (after initial reset)
first_run = True

while True:

    # Read current state
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        row = next(reader)
        a, b, c = map(int, row)

    print(f"\nCurrent Values → Reset: {a}, Gate: {b}, Override: {c}")

    user_input = input(
        "Type (a)=reset, (b)=gate, (c)=override, or (q)=quit: "
    ).lower()

    if user_input == "q":
        break

    # RESET
    if user_input == "a":
        while True:
            try:
                number = int(input("Enter integer (0-1): "))
                if number in [0, 1]:
                    if first_run:
                        a = number  # first run: overwrite
                        first_run = False
                    else:
                        a += number  # subsequent runs: add to previous state
                    break
                else:
                    print("Value must be 0 or 1.")
            except ValueError:
                print("Invalid integer.")

    # GATE
    elif user_input == "b":
        while True:
            try:
                number = int(input("Enter integer (0-6): "))
                if 0 <= number <= 7:
                    if first_run:
                        b = number
                        first_run = False
                    else:
                        b += number
                    break
                else:
                    print("Value must be between 0 and 7.")
            except ValueError:
                print("Invalid integer.")

    # OVERRIDE
    elif user_input == "c":
        while True:
            try:
                number = int(input("Enter integer (0-2): "))
                if 0 <= number <= 2:
                    if first_run:
                        c = number
                        first_run = False
                    else:
                        c += number
                    break
                else:
                    print("Value must be between 0 and 2.")
            except ValueError:
                print("Invalid integer.")

    # Overwrite file with UPDATED totals (single row)
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([a, b, c])