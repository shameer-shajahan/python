def print_consecutive_numbers(n):
    for i in range(1, n + 1):
        # Print each number without space or newline at the end
        print(i, end='')

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    # Read the integer from stdin
    n = int(input().strip())
    # Call the function to print the sequence
    print_consecutive_numbers(n)
