def generate_sequence(n):
    
    # Start the sequence
    sequence = [1, 2, 3]

    # Print the first three elements always
    for i in range(3):
        print(sequence[i], end='')
    
    if n < 3:
        # If n is less than or equal to 3, print n at the end
        print(n, end='')
    else:
        # If n is greater than 3, continue printing from 4 to n
        for i in range(4, n + 1):
            print(i, end='')

    print()  # Move to a new line after the output

if __name__ == '__main__':
    n = int(input())
    generate_sequence(n)
