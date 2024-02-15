def stream_cypher(sequence):
    # Get the length of the sequence
    n = len(sequence)
    
    # Initialize the 'c' array with zeros and set the first element to 1
    c = [0 for _ in range(n)]
    c[0] = 1
    
    # Initialize the 'b' array with zeros and set the first element to 1
    b = [0 for _ in range(n)]
    b[0] = 1

    # Initialize the LFSR length, the position of the last discrepancy, and the current position
    L = 0
    m = -1
    N = 0

    # Iterate until the entire sequence is processed
    while N < n:
        # Compute the discrepancy between sequence and feedback polynomial
        d = sequence[N]
        for i in range(1, L+1):
            d ^= (c[i] & sequence[N-i])

        # If discrepancy is found
        if d == 1:
            # Store the current polynomial in 't'
            t = list(c)
            
            # Adjust the polynomial 'c' based on 'b'
            for i in range(n - N + m):
                c[N - m + i] ^= b[i]

            # Update the LFSR length if necessary
            if L <= N // 2:
                L = N + 1 - L
                m = N
                b = t

        # Move to the next position in the sequence
        N += 1

    # Return the coefficients of the LFSR
    return [coef for coef, val in enumerate(c[:L+1]) if val == 1]

# Example usage:
sequence_a = [
    1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0,
    0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1,
    1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0,
    1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1,
    0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0,
    1, 0, 0, 0, 0

]
sequence_b = [
    1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0,
    0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0,
    0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1,
    1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0,
    1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1,
    1, 1, 1, 1, 1
]

print("Coefficients for sequence a:", stream_cypher(sequence_a))
print("Coefficients for sequence b:", stream_cypher(sequence_b))
