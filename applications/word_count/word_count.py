import re


def word_count(s):
    # Your code here
    cache = {}

    string = re.sub("[^a-z'A-Z]+", " ", s)
    words = string.lower().split(' ')

    for word in words:
        if word == '':
            pass
        elif word not in cache:
            cache[word] = 1
        else:
            cache[word] += 1

    return cache


if __name__ == "__main__":
    print(word_count('a a\ra\na\ta \t\r\n'))
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
