# !/usr/bin/env python3
import random


def get_all_words(length=""):
    # word file has been split to file with words of each length using createFilePerSize.py
    words = []
    for i in open(f"woorden/woorden{length}.txt", 'r'):
        words.append(i.rstrip("\n").upper())
    return words


def get_new_filter():
    return "_" * len(random.choice(get_all_words()))


def guess_letter(letter: str, filter_str: str, exclude: list):
    if 15 < len(filter_str) or len(filter_str) < 5:
        return error("Invalid filter size")

    if letter in filter_str:
        return error("Letter already used")

    letter = letter.upper()
    words = get_all_words(str(len(filter_str)))
    exclude = [i.upper() for i in exclude]
    solution = recursive_filter(filter_str, letter, exclude, 0, words, 0)
    return {'filter': solution[0], 'mistake': solution[0] == filter_str, 'done': ("_" not in solution[0])}


def error(message: str):
    return {'error: ': message}


def recursive_filter(filter_str: str, letter: str, exclude: list, pos: int, words: list, bound: int):
    if len(words) <= bound:
        # if amount of words is lower then the current bound
        return "", 0
    if pos == len(filter_str):
        # if at the end of the filter
        return filter_str, len(words)
    if pos > 2 and filter_str[pos - 3:pos] == letter * 3:
        # there are no words with the same letter repeated more then three times
        newwords = []
        for word in words:
            if word[pos] not in exclude:
                newwords.append(word)
        return recursive_filter(filter_str, letter, exclude, pos + 1, newwords, bound)
    elif filter_str[pos] == "_":
        # filter is still empty at this position
        words_with_letter = []
        words_without_letter = []
        for word in words:
            if word[pos] == letter:
                words_with_letter.append(word)
            elif word[pos] not in exclude:
                words_without_letter.append(word)
        without_word = recursive_filter(filter_str, letter, exclude, pos + 1, words_without_letter, bound)
        filter_str = filter_str[:pos] + letter + filter_str[pos + 1:]
        with_word = recursive_filter(filter_str, letter, exclude, pos + 1,
                                     words_with_letter, max(without_word[1], bound))
        returnstep = without_word
        if with_word[1] > without_word[1]:
            returnstep = with_word
        elif with_word[1] == without_word[1]:
            returnstep = with_word if random.getrandbits(1) else without_word
        return returnstep
    else:
        # letter in filter is already decided
        curletter = filter_str[pos]
        newwords = []
        for word in words:
            if word[pos] == curletter:
                newwords.append(word)
        return recursive_filter(filter_str, letter, exclude, pos + 1, newwords, bound)
