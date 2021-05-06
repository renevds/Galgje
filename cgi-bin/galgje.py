#!/usr/bin/env python3
import copy
import random
import re
import time


def get_all_words(length=""):
    length = str(length)
    words = []
    for i in open(f"woorden/woorden{length}.txt", 'r'):
        words.append(i.rstrip("\n").upper())
    return words


def get_new_fitler():
    return "." * len(random.choice(get_all_words()))


def filter_words(wordlist: list, filter_str: str):
    return [i for i in wordlist if re.match("^" + filter_str + "$", i)]


def get_exclude_regex(exclude: set):
    exclude_letters = "".join(exclude)
    return r'[^' + exclude_letters + r']' if len(exclude) > 0 else "."


def guess_letter(letter: str, filter_str: str, exclude: list):
    words = filter_words(get_all_words(len(filter_str)), filter_str)

    exclude.append(letter.upper())

    exclude_regex = get_exclude_regex(exclude)

    new_filter = recursive_filter(words, filter_str, letter.upper(), exclude_regex,
                                  len(filter_words(words, filter_str.replace(".", exclude_regex))))[0]

    ret_filter = new_filter.replace(exclude_regex, ".")

    return {'done': new_filter.count(exclude_regex) == 0, 'filter': ret_filter.replace(exclude_regex, "."),
            'mistake': ret_filter == filter_str, 'exclude': exclude}


def recursive_filter(words: list, filter: str, letter: str, exclude_regex: str, limit: int):
    with open("debug.txt", "a") as f:
        try:
            f.write(f"filter: {filter} | amount: {len(filter_words(words, filter))}" + "\n")
            index = filter.index('.')
            filtered_words = filter_words(words, filter)
            if len(filtered_words) < limit:
                return "", 0
            if index > 1 and filter[index - 1] == letter and filter[index - 2] == letter:
                return recursive_filter(filtered_words, filter.replace(".", exclude_regex, 1), letter, exclude_regex, limit)
            else:
                addLetter = recursive_filter(filtered_words, filter.replace(".", letter, 1), letter, exclude_regex, limit)
                addExclude = recursive_filter(filtered_words, filter.replace(".", exclude_regex, 1), letter,
                                              exclude_regex, addLetter[1])
                return addLetter if addLetter[1] > addExclude[1] else addExclude
        except ValueError:
            return filter, len(filter_words(words, filter))
