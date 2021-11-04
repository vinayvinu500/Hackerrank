# https://www.hackerrank.com/challenges/inheritance/problem?h_r=internal-search
class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


from statistics import mean


class Student(Person):
    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        char = ''
        avg = mean(self.scores)
        if 90 <= avg <= 100:
            char = 'O'
        elif 80 <= avg < 90:
            char = 'E'
        elif 70 <= avg < 80:
            char = 'A'
        elif 55 <= avg < 70:
            char = 'P'
        elif 45 <= avg < 55:
            char = 'D'
        elif avg < 40:
            char = 'T'
        return char

    pass


line = input().split()
FirstName = line[0]
LastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
score = list(map(int, input().split()))
s = Student(FirstName, LastName, idNum, score)
s.printPerson()
print("Grade:", s.calculate())


"""
Examples
Heraldo Memelli 8135627
10
100 80 40 20 50 60 10 70 30 90
"""