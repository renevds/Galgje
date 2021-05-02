#!/usr/bin/env python3
import random
import re


def get_all_words():
    words = []
    for i in open("woorden.txt", 'r'):
        words.append(i.rstrip("\n").upper())
    return words


def get_new_fitler():
    return "." * len(random.choice(get_all_words()))


def filter_words(wordlist: list, filter_str: str):
    return [i for i in wordlist if re.match("^" + filter_str + "$", i)]


def guess_letter(letter: str, filter_str: str):
    words = filter_words(get_all_words(), filter_str)
    best_words = []
    best_filter = ""
    for i in range(len(filter_str)):
        temp_filter = filter_str[:i] + letter.upper() + filter_str[i + 1:]
        temp_words = filter_words(words, temp_filter)
        if len(temp_words) > len(best_words):
            best_words = temp_words
            best_filter = temp_filter

    if len(best_words) == 0:
        return {'done': False, 'filter': filter_str, 'mistake': True}
    elif len(best_words) == 1:
        return {'done': True, 'filter': best_words[0], 'mistake': False}
    else:
        for i in range(len(best_filter)):
            if best_filter[i] == '.':
                temp_filter = filter_str[:i] + letter.upper() + filter_str[i + 1:]
                if len(filter_words(words, temp_filter)) == len(best_words):
                    best_filter = temp_filter
        return {'done': False, 'filter': best_filter, 'mistake': False}
