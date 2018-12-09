STARTING_FREQUENCY = 0

lines = open('day_1_input.txt', 'rt').readlines()
lines_stripped = (line.strip() for line in lines)
frequencies = map(int, lines_stripped)
resulting_frequency = sum(frequencies)

print(f'Resulting frequency is: {resulting_frequency}')
