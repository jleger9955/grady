# read in grades.txt
# print out a list of students
# and their avg grade for class
# and rank them in order
# from high to low
# i.e., bob 98, sue 97, sara 76
from collections import defaultdict


def get_grades(fn):
    grades = defaultdict(list)
    with open(fn) as f:
        for line in f:
            name, grade = line.strip().split(' ')
            grade = float(grade)
            grades[name].append(grade)
    return grades


def get_averages(grades):
    avgs = []
    for name, scores in grades.items():
        avg = sum(scores) / len(scores)
        avgs.append((name, avg))
    return avgs


def rank_scores(avgs):
    return sorted(avgs, key=lambda t: t[1])[::-1]
