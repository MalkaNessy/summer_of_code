# A Few Things to Try
# Write a program that tells you the following:

# Hours in a year. How many hours are in a year?
print (24*365)
# Minutes in a decade. How many minutes are in a decade?
print (60*24*10)
# Your age in seconds. How many seconds old are you? (I'm not going to check your answer, so be as accurate—or not—as you want.)
print (60*60*24*365*40) #1261440000
# Andreea Visanoiu​: I'm 48618000 seconds old hahaha. Calculate @Andreea Visanoiu's age.
print (48618000/(60*60*24*365)) #1.5416666666666667

# Here are some tougher questions:

# How many days does it take for a 32-bit system to timeout, if it has a bug with integer overflow?
# How about a 64-bit system?
# Calculate your age accurately based on your birthday 
#   (maybe use time of day e.g. 8:23am if you know it, use 12:00 noon midday) - you will need Python modules.
from datetime import datetime, date, time

birthday = date(1978, 7, 19)
def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

age = calculate_age(birthday)
print(age)


