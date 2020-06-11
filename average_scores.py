#Start Program
"""
Program: average_scores.py
Author: Paul Thairu
Last date modified: 06/03/2020

Write the tests and program average_scores.py to read in one person's names,
first and last, their age and three scores out of 100.
Take the three scores and find the average, storing into a variable.
"""


def average(total_score):

    return total_score/3


try:
    if __name__ == '__main__':

        last_name = str(input("Please enter your last name: "))
        # Get user input for last name
        first_name = str(input("Please enter your last name: "))
        age = int(float(input("Please enter your age: ")))
        if age < 0:
            print("Age can not be -VE")
        age = int(input("Please enter your age: "))
        # Get user input for first score
        test_score_one = int(float(input("Please enter test score one: ")))
        # Get user input for second score
        test_score_two = int(float(input("Please enter test score two: ")))
        # Get user input for third score
        test_score_three = int(float(input("Please enter test score three: ")))
except:
    print("Oops!  AGE and SCORES can only be numbers.  Try again...")
    # Totaling all the scores
    total_score = float(test_score_one) + float(test_score_two) + float(test_score_three)
    print("Total score for the three tests is: " + str(total_score))

    # Calling average() function
    average_score = str(average(total_score))

    # Printing output
    print(last_name + ", " + first_name + " age: " + str(age) + " average grade: " + str(average_score))

#End program
