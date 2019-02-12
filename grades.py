# read in grades.txt
# print out a list of students
# and their avg grade for class
# and rank them in order
# from high to low
# i.e., bob 98, sue 97, sara 76

import operator

master_lst = []
names = []

with open('grades.txt') as f:
    for line in f:
        student = line.strip().split(' ')
        master_lst.append(student)
        if student[0] not in names:
            names.append(student[0])

grd_tots = {name: 0 for name in names}
for rec in master_lst:
    for name in grd_tots:
        if rec[0] == name:
            grd_tots[name] += int(rec[1])

grd_cnts = {name: 0 for name in names}
for rec in master_lst:
    for name in grd_cnts:
        if rec[0] == name:
            grd_cnts[name] += 1

grd_avgs = {name: 0 for name in names}
for name in grd_avgs:
    grd_avgs[name] = grd_tots[name] / grd_cnts[name]


sorted_avgs = sorted(grd_avgs.items(), key=operator.itemgetter(1))

for i in sorted_avgs[::-1]:
    print('{} {}'.format(i[0], i[1]))

'''
print(names)
print(master_lst)
print(grd_cnts)
print(grd_tots)
print(grd_avgs)
print(sorted_avgs)
'''
# for rec in master_lst
#   tots.append(rec[0])
