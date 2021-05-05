if __name__ == '__main__':
    words = {}
    for i in open("woorden.txt", 'r'):
        woord = i.rstrip("\n")
        size = len(woord)
        if size not in words:
            words[size] = []
        words[size].append(woord)

    for size, wordlist in words.items():
        with open(f"woorden{size}.txt", "w") as f:
                for word in wordlist:
                    f.write(word + "\n")