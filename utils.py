import random as r
import datetime


def get_random_phone_number():
    return r.randint(10000000000, 99999999999)


def get_random_date(year=2022):
    day = r.randint(1, 28)
    month = r.randint(1, 12)
    return str(day) + '.' + str(month) + '.' + str(year)


def get_current_date():
    return datetime.date.today().strftime('%d.%m.%Y')


def get_next_date():
    next_date = datetime.date.today() + datetime.timedelta(days=1)
    return next_date.strftime('%d.%m.%Y')
