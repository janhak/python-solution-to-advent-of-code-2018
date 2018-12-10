# https://adventofcode.com/2018/day/2
from collections import Counter, defaultdict
import pytest
import operator
import itertools


def lines(input_fname):
    with open(input_fname, 'rt') as f:
        return f.read().splitlines()


# First part
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


# Brute Force
def one_char_diff(first, second):
    """Are first and second equal except for one character"""
    differences = sum((x != y) for x, y in zip(first, second))
    return differences == 1


def find_two_similar_boxes(box_ids):
    """Return a pair of box_ids that differ by one character"""
    for x, y in itertools.product(box_ids, box_ids):
        if one_char_diff(x, y):
            return x, y


def common_characters(first, second):
    return ''.join(x for x, y in zip(first, second) if x == y)


# Quick solution
def blank_one_char(a_string):
    """Yield all strings with one char blanked"""
    for i in range(len(a_string)):
        yield a_string[:i] + '_' + a_string[i+1:]


def find_two_similar_fast(box_ids):
    """Find first pair of box_ids that differ by one character"""
    blanked = defaultdict(list)
    for box in box_ids:
        for blank in blank_one_char(box):
            blanked[blank].append(box)

    return next(v for v in blanked.values() if len(v) == 2, None)


if __name__ == '__main__':
    box_ids = list(lines('day_2_input.txt'))
    counted_ids = (count_letters(box_id) for box_id in box_ids)
    count = (sum(x) for x in zip(*counted_ids))
    print(f'Checksum for box ids is: {operator.mul(*count)}')

    # Brute Force
    boxes = find_two_similar_boxes(box_ids)
    print(f'Letters that are the same between two similar boxes are: {common_characters(*boxes)}')

    # Quick
    boxes = find_two_similar_fast(box_ids)
    print(f'Letters that are the same between two similar boxes are: {common_characters(*boxes)}')


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
