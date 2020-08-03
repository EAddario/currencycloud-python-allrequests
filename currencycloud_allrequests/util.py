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
