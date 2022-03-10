"""
cleans punctuation, strips trailing white spaces
lowercases everything
"""
import string
import csv
from copy import copy
from core import Core


def clean_text(wd_):
    """
    cleans punctuation, strips trailing white spaces
    lowercases everything
    """
    wd_ = wd_.strip().lower()
    return wd_.translate(str.maketrans('', '', string.punctuation))

with open('data/random_text.txt', 'r') as random_txt:
    wds = list(map(clean_text, random_txt.read().split()))
    wds_copy = copy(wds)
    wds.reverse()

with open('data/wordlist.csv', 'w') as wdlist:
    for wd1, wd2 in zip(wds_copy, wds):
        dist = Core().edit_distance(wd1, wd2)
        writer = csv.writer(wdlist)
        writer.writerow([wd1, wd2, str(dist)])
