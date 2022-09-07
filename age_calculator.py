""" pacakage datetime"""
import datetime

def age_calculator(y, m, d):
    """ Function that calculate your age """
    today = datetime.datetime.now().date()
    dob = datetime.date(y, m, d) #date of birth
    age = int((today - dob).days / 365)

    print('You age is: ', age)

y = int(input('type your birth Year: '))
m = int(input('type your birth Month(1-12): '))
d = int(input('type your birth Date(1-31): '))

age_calculator(y, m, d)
