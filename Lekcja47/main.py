import re
import time


def task(string):
    letters = re.findall(r'\D+', string)
    numbers = re.findall(r'\d+', string)

    return "".join(l * int(n) for l, n in zip(letters, numbers))


def first_unique(string):
    return [letter for letter in string if letter.count(letter) == 1][0]


def sort_by_square(l):
    return sorted(l, key=lambda x: x ** 2)


print(task("a3b4c10"))
print(first_unique("a3b4c10"))


def create_hero(*args, **kwargs):
    name = " ".join(args)

    classes = "\n".join(f"Klasa: {cls}, lvl: {lvl}" for cls, lvl in kwargs.items())

    return f"Imię: {name}\n{classes}"


def timeline(func):
    def wrapper(*args, **kwargs):
        from datetime import datetime
        start_time = datetime.now()
        start_formatted = start_time.strftime('%H:%M:%S')
        start_milliseconds = start_time.microsecond // 1000
        print(f"Start: {start_formatted}.{start_milliseconds}")
        func(*args, **kwargs)
        end_time = datetime.now()
        end_formatted = end_time.strftime('%H:%M:%S')
        end_milliseconds = end_time.microsecond // 1000
        print(f"End: {end_formatted}.{end_milliseconds}")

    return wrapper


@timeline
def add(a, b):
    time.sleep(1)
    print(a + b)


def gen(limit):
    counter = 0
    while counter < limit:
        yield counter
        counter += 1


add(2, 3)
gen1 = gen(5)
gen2 = gen(5)
print(next(gen1))
print(next(gen2))
print(next(gen1))
print(next(gen2))
