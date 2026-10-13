# Worksheet 1.3: Task 1

L = int(input("Length of sequence: "))  # this should be your only input


# Your code for the Recaman Sequence
# You should store the sequence in an appropriate data structure named 'sequence'

sequence = {-1: 0, 0: 0}
n = 0
print(sequence[n])
for n in range(L):
    if not sequence[n - 1] - n in sequence.values() and sequence[n - 1] - n > 0:
        sequence[n] = sequence[n - 1] - n
    else:
        sequence[n] = sequence[n - 1] + n


# You may wish to use further output for testing purposes while you develop your code

[print(item) for item in sequence.items()]

# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence
