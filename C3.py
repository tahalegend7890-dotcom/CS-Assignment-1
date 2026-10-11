# Convert a positive decimal integer to binary using repeated division by 2.
def decimal_to_binary(number):
    """Return the binary representation of a positive integer as text."""
    if number <= 0:
        raise ValueError("Enter a positive integer")

    binary_digits = ""
    while number > 0:
        remainder = number % 2
        binary_digits = str(remainder) + binary_digits
        number = number // 2
    return binary_digits


print(f"decimal_to_binary(10) -> {decimal_to_binary(10)}")
print(f"decimal_to_binary(25) -> {decimal_to_binary(25)}")
