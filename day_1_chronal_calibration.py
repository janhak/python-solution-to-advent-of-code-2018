import itertools
import pytest


def deltas_from_input(input_fname):
    with open(input_fname, 'rt') as f:
        return list(map(eval, f))


def frequencies(changes):
    f = 0
    yield f
    for ch in changes:
        f += ch
        yield f


def first_duplicate(sequence):
    seen = set()
    for value in sequence:
        if value in seen:
            return value
        seen.add(value)


if __name__ == '__main__':
    deltas = deltas_from_input('day_1_input.txt')
    print(f'First frequency is: {sum(deltas)}')
    print(f'First repeating frequency is: {first_duplicate(frequencies(itertools.cycle(deltas)))}')


# Tests
@pytest.mark.parametrize('sequence, duplicate', [
    ('masfdmfdsfa', 'm'),
    ([1, 2, 3, 4, 1], 1),
    ([0, 0], 0),
])
def test_first_duplicate(sequence, duplicate):
    assert first_duplicate(sequence) == duplicate

@pytest.mark.parametrize('deltas, partial_sums', [
    ([1, 2, 3, 4], [0, 1, 3, 6, 10]),
    ([0, 0], [0, 0, 0]),
    ([-1, 2, 1], [0, -1, 1, 2]),
])
def test_frequencies(deltas, partial_sums):
    assert list(frequencies(deltas)) == partial_sums
