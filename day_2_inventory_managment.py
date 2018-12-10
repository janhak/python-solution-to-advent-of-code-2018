# https://adventofcode.com/2018/day/2
from collections import Counter
import pytest
import operator

def lines(input_fname):
    with open(input_fname, 'rt') as f:
        for line in f:
            yield line.strip()


def count_letters(box_id):
    letter_twice = 0
    letter_thrice = 0
    c = Counter(box_id)
    for _, v in c.items():
        if v == 2:
            letter_twice = 1
        if v == 3:
            letter_thrice = 1
    return (letter_twice, letter_thrice)


if __name__ == '__main__':
    box_ids = lines('day_2_input.txt')
    counted_ids = (count_letters(box_id) for box_id in box_ids)
    count = (sum(x) for x in zip(*counted_ids))
    print(f'Checksum for box ids is: {operator.mul(*count)}')


# Tests
@pytest.mark.parametrize('an_id, count', [
    ('abcdef', (0, 0)),
    ('bababc', (1, 1)),
    ('abbcde', (1, 0)),
    ('abcccd', (0, 1)),
    ('aabcdd', (1, 0)),
    ('abcdee', (1, 0)),
    ('ababab', (0, 1)),
])
def test_count_letters(an_id, count):
    assert count_letters(an_id) == count
