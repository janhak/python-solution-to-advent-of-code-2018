# https://adventofcode.com/2018/day/2
from collections import Counter
import pytest
import operator
import itertools


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


def one_char_diff(first, second):
    differences = 0
    for x, y in zip(first, second):
        if x != y:
            differences += 1
        if differences > 1:
            return False
    return differences == 1


def find_two_similar_boxes(box_ids):
    for x, y in itertools.product(box_ids, box_ids):
        if one_char_diff(x, y):
            return x, y


def filter_out_diff(first, second):
    for x, y in zip(first, second):
        if x == y:
            yield x


if __name__ == '__main__':
    box_ids = list(lines('day_2_input.txt'))
    counted_ids = (count_letters(box_id) for box_id in box_ids)
    count = (sum(x) for x in zip(*counted_ids))
    print(f'Checksum for box ids is: {operator.mul(*count)}')

    boxes = find_two_similar_boxes(box_ids)
    same = ''.join(filter_out_diff(*boxes))
    print(f'Letters that are the same between two similar boxes are: {same}')


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

@pytest.mark.parametrize('first, second, diff', [
    ('aabc', 'aacc', True),
    ('aaaa', 'aaaa', False),
    ('abbc', 'aaaa', False),
])
def test_one_char_diff(first, second, diff):
    assert one_char_diff(first, second) == diff
