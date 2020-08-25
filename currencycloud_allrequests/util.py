import datetime
import random
import string

from colorama import Fore, Style

from currencycloud_allrequests.config import index
from currencycloud_allrequests.config import colors


def output(msg):
    global index
    print(Style.BRIGHT + getattr(Fore, colors[index % len(colors)]) + msg)
    index += 1


def random_string(length):
    chars = string.ascii_uppercase
    return ''.join(random.choice(chars) for i in range(length))


def add_working_days(from_date, add_days):
    business_days_to_add = add_days
    current_date = datetime.datetime.strptime(from_date, "%Y-%m-%dT%H:%M:%S+00:00")
    while business_days_to_add > 0:
        current_date += datetime.timedelta(days=1)
        weekday = current_date.weekday()
        if weekday >= 5:
            continue
        business_days_to_add -= 1
    return current_date
