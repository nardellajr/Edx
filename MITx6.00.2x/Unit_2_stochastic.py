import random


def roll_die():
    return random.choice([1, 2, 3, 4, 5, 6])


def test_roll(n=10):
    result = ''
    for i in range(n):
        result = result + str(roll_die())

    print(result)


def gen_even():
    """Returns an even random number x, where 0 < = x < 100"""
    # return random.randint(0, 100)  # Generates random number, but not even
    return random.randrange(0, 100, 2)


def test_seed():
    random.seed(4)
    print([random.randint(1, 9) for _ in range(7)])


def even_deterministic_number():
    for _ in range(20):
        print(random.randint(9, 21))


if __name__ == '__main__':
    test_roll()

    for i in range(10):
        print(gen_even())

    test_seed()

    even_deterministic_number()
