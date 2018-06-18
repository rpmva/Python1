#Different Modules:
#random, os, json, sqlite3, datetime, getpass, this, pprint
#using the random module:
# for i in range(10):
# 	randint(1,10)
#
#
# 8
# 2
# 5
# 9
# 6
# 5
# 3
# 10
# 9
# 1
#Example 2:
# frequency = {}
# for i in range(1000):
#   num = randint(1, 10)
#   if frequency.has_key(num):
# 	frequency[num] = frequency[num] + 1
#   else:
# 	frequency[num] = 1
#
#
# print frequency
# {1: 104, 2: 97, 3: 92, 4: 106, 5: 93, 6: 107, 7: 98, 8: 104, 9: 97, 10: 102}
#Example 3:
# import random
# random.randint(1,100) <- when we call randint we must put random at the beginning of the call
# 43
#random function: returns random float between 0 and 1
# from random import random
# for i in range(10):
# 	print random()
#
# 0.69749992523
# 0.136305332878
# 0.385093111015
# 0.819310151425
# 0.308796665599
# 0.957826347985
# 0.595598703669
# 0.752341269276
# 0.909160951962
# 0.0738856948118

#uniform: takes 2 parameters and returns a float between those 2 numbers
# from random import uniform
# for i in range(10):
# 	print uniform(1,5)
#
#
# 2.67850411766
# 1.47851178597
# 2.72335939882
# 4.10585783848
# 3.2662483727
# 4.57349298534
# 2.34016892939
# 3.45093554977
# 2.01409688106
# 2.60385626201

#choice: takes a random item from a list or tuple
# from random import choice
# grades = ['a','b','c','d','f']
# choice(grades) -> 'a'

#datetime Module
#time
# from datetime import time
# lunch = time(11,30)
# print lunch -> 11:30:00

#example 2
# lunch = time(11,30)
# lunch.hour -> 11
# lunch.minute -> 30
# lunch.second -> 0

#exaple 3
# lunch = time(11,30)
# print "Lunch will be served at {minutes} minutes past {hour}".format(minutes=lunch.minute, hour=lunch.hour) -> Lunch will be served at 30 minutes past 11

#example 4
# import datetime
# breakfast = datetime.time(7,30)
# lunch = datetime.time(11,30)
# elevensies = datetime.time(11,30)
# breakfast > lunch -> False
# breakfast < lunch -> True
# elevensies == lunch -> True

#datetime
# import datetime
# hm = datetime.datetime(year=2009, day=9, month=1)
# jt = datetime.datetime(year=2001, day=14, month=4)
# hm-jt -> datetime.timedelta(2827); timedelta represents a difference between 2 dates

#example 2
# import datetime
# week = datetime.timedelta(days=7)
# n = datetime.datetime.now()
# n + week -> datetime.datetime(2018, 6, 24, 23, 24, 28, 932094)

#example 3
# import datetime
# payday = datetime.date(year=2011, day=31, month=5)
# period = datetime.timedelta(days=14)
# next_payday = payday + period
# next_payday -> datetime.date(2011, 6, 14)
