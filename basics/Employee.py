#!/usr/bin/pyton
# -*- coding:UTF-8 -*-

class Employee:

    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def __del__(self):
        pass

    def display(self):
        print "Total employee %d" % Employee.empCount

if __name__ == '__main__':
    print "Object oriented programming"
    employee1 = Employee('TOM', 100)
    employee2 = Employee('TOM', 100)
    employee1.display()
    a = 'hi'
    b = 'hi'
    print id(a)
    print id(b)
