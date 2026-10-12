# Calculate AND, OR, and XOR outputs for two input bits.
bit_a = int(input("Enter A: "))
bit_b = int(input("Enter B: "))

if (bit_a != 0 and bit_a != 1) or (bit_b != 0 and bit_b != 1):
    print("Bits must be 0 or 1")
else:
    if bit_a == 1 and bit_b == 1:
        and_output = 1
    else:
        and_output = 0

    if bit_a == 1 or bit_b == 1:
        or_output = 1
    else:
        or_output = 0

    if bit_a != bit_b:
        xor_output = 1
    else:
        xor_output = 0

    print("AND =", and_output)
    print("OR =", or_output)
    print("XOR =", xor_output)
