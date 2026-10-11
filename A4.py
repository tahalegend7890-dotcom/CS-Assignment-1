# Calculate AND, OR, and XOR outputs for two input bits.
bit_a = int(input("Enter A: "))
bit_b = int(input("Enter B: "))

if (bit_a != 0 and bit_a != 1) or (bit_b != 0 and bit_b != 1):
    print("Bits must be 0 or 1")
else:
    and_output = 1 if bit_a == 1 and bit_b == 1 else 0
    or_output = 1 if bit_a == 1 or bit_b == 1 else 0
    xor_output = 1 if bit_a != bit_b else 0
    print(f"AND = {and_output}")
    print(f"OR = {or_output}")
    print(f"XOR = {xor_output}")
