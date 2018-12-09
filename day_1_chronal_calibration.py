import itertools


def frequencies_from_input(input_fname):
    with open(input_fname, 'rt') as f:
        return list(map(eval, f))


def first_repeating_frequency(frequencies, current_frequency=0):
    frequencies_seen = set()
    frequencies_seen.add(current_frequency)
    for f in itertools.cycle(frequencies):
        current_frequency += f
        if current_frequency in frequencies_seen:
            return current_frequency
        frequencies_seen.add(current_frequency)


if __name__ == '__main__':
    frequencies = frequencies_from_input('day_1_input.txt')

    print(f'First frequency is: {sum(frequencies)}')
    print(f'First repeating frequency is: {first_repeating_frequency(frequencies)}')
