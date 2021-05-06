import re


def regex(regex):
    correct = []
    for i in open("woorden.txt"):
        if re.match(regex, i):
            correct.append(i)
    print(f"match: {len(correct)}")
    print(f"first 10: {correct[:10]}")


if __name__ == '__main__':
    regex(r"^[^e][^e][^e][^e][^e][^e][^e][^e][^e][^e][^e][^e][^e]e.$")
