import csv
from typing import List

from package import Package
from Distance import load_distance_data

load_distance_data('Data/WGUPS_Distance_Table.csv')


def greedy_algorithm(budget):
    total = budget
    c25dollar = 0
    c10dollar = 0
    c5dollar = 0
    c1dollar = 0
    while budget >= 25:
        if c25dollar > 3:
            break
        c25dollar += 1
        budget = budget - 25
    while budget >= 10:
        c10dollar += 1
        budget = budget - 10
    while budget >= 5:
        c5dollar += 1
        budget = budget - 5
    while budget > 0:
        if c1dollar > 3:
            break
        c1dollar += 1
        budget = budget - 1
    c_dvd = c25dollar + c10dollar + c5dollar + c1dollar

    print("${:.2f}-Total Dollar Budget: {}-DVDs =>".format(total, c_dvd))
    print(" {} X 25 dollar movie = ${:.2f}".format(c25dollar, c25dollar * 25.00))
    print(" {} X 10 dollar movie = ${:.2f}".format(c10dollar, c10dollar * 10.00))
    print(" {} X 5 dollar movie = ${:.2f}".format(c5dollar, c5dollar * 5.00))
    print(" {} X 1 dollar movie = ${:.2f}".format(c1dollar, c1dollar * 1.00))


print("\nGreedy Algorithm: Min Expenses => Max Profits")
greedy_algorithm(102)
greedy_algorithm(94)
greedy_algorithm(71)
greedy_algorithm(200)
