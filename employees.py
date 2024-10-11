"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my/our honor, Niccolo Faelnar, this
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: nvf89
"""

from abc import ABC, abstractmethod
import random

DAILY_EXPENSE = 60
HAPPINESS_THRESHOLD = 50
MANAGER_BONUS = 1000
TEMP_EMPLOYEE_PERFORMANCE_THRESHOLD = 50
PERM_EMPLOYEE_PERFORMANCE_THRESHOLD = 25
RELATIONSHIP_THRESHOLD = 10
INITIAL_PERFORMANCE = 75
INITIAL_HAPPINESS = 50
PERCENTAGE_MAX = 100
PERCENTAGE_MIN = 0
SALARY_ERROR_MESSAGE = "Salary must be non-negative."



class Employee(ABC):
    """
    Abstract base class representing a generic employee in the system.
    """

    def __init__(self, name, manager, salary, savings):
        self.relationships = {}
        self.savings = savings
        self.is_employed = True
        self.__name = name
        self.__manager = manager
        self.performance = INITIAL_PERFORMANCE
        self.happiness = INITIAL_HAPPINESS
        self.salary = salary

    @property
    def name(self):
        "The name of the employee"
        return self.__name
    @property
    def manager(self):
        "The employee's manager"
        return self.__manager
    @property
    def performance(self):
        "The employee’s performance on a percentage scale of 0 to 100"
        return self.__performance

    @performance.setter
    def performance(self, value):
        if value < PERCENTAGE_MIN:
            self.__performance = PERCENTAGE_MIN
        elif value > PERCENTAGE_MAX:
            self.__performance = PERCENTAGE_MAX
        else:
            self.__performance = value
    @property
    def happiness(self):
        "The employee’s happiness on a percentage scale of 0 to 100"
        return self.__happiness

    @happiness.setter
    def happiness(self, value):
        if value < PERCENTAGE_MIN:
            self.__happiness = PERCENTAGE_MIN
        elif value > PERCENTAGE_MAX:
            self.__happiness = PERCENTAGE_MAX
        else:
            self.__happiness = value
    @property
    def salary(self):
        "The employee's salary"
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value >= 0:
            self.__salary = value
        else:
            raise ValueError()
    @abstractmethod
    def work(self):
        '''This method is intended to simulate 1 hour of work, 
        during which an employee's performance, salary, and happiness can be affected.'''

    def interact(self, other):
        "Simulates an interaction between this employee and another employee (other)."
        if other.name not in self.relationships:
            self.relationships[other.name] = 0
        if self.relationships[other.name] >= RELATIONSHIP_THRESHOLD:
            self.happiness += 1
        elif self.happiness >= HAPPINESS_THRESHOLD and other.happiness >= HAPPINESS_THRESHOLD:
            self.relationships[other.name] += 1
        else:
            self.relationships[other.name] -= 1
            self.happiness -= 1

    def daily_expense(self):
        "Simulates the employee’s daily expenses by reducing their happiness and savings."
        self.happiness -= 1
        self.savings -= DAILY_EXPENSE

    def __str__(self):
        return_str = self.name
        return_str += f"\n\tSalary: ${self.salary}"
        return_str += f"\n\tSavings: ${self.savings}"
        return_str += f"\n\tHappiness: {self.happiness}%"
        return_str += f"\n\tPerformance: {self.performance}%"
        return return_str


class Manager(Employee):
    """
    A subclass of Employee representing a manager.
    """
    def work(self):
        change = random.randint(-5, 5)
        self.performance += change
        if change <= 0:
            self.happiness -= 1
            for key in self.relationships:
                self.relationships[key] -= 1
        else:
            self.happiness += 1


class TemporaryEmployee(Employee):
    """
    A subclass of Employee representing a temporary employee.
    """
    def work(self):
        change = random.randint(-15, 15)
        self.performance += change
        if change <= 0:
            self.happiness -= 2
        else:
            self.happiness += 1

    def interact(self, other):
        super().interact(other)
        if other == self.manager:
            if other.happiness > HAPPINESS_THRESHOLD:
                if self.performance >= TEMP_EMPLOYEE_PERFORMANCE_THRESHOLD:
                    self.savings += MANAGER_BONUS
            if other.happiness <= HAPPINESS_THRESHOLD:
                self.salary = self.salary // 2
                self.happiness -= 5
                if self.salary <= 0:
                    self.is_employed = False


class PermanentEmployee(Employee):
    """
    A subclass of Employee representing a permanent employee.
    """
    def work(self):
        change = random.randint(-10, 10)
        self.performance += change
        if change >= 0:
            self.happiness += 1

    def interact(self, other):
        super().interact(other)
        if other == self.manager:
            if other.happiness > HAPPINESS_THRESHOLD:
                if self.performance >= PERM_EMPLOYEE_PERFORMANCE_THRESHOLD:
                    self.savings += MANAGER_BONUS
            if other.happiness <= HAPPINESS_THRESHOLD:
                self.happiness -= 1