# Convert a positive decimal integer to binary using repeated division by 2.
def decimal_to_binary(number):
    # Keep dividing by two and place each remainder at the front of the answer.
    binary_digits = ""
    while number > 0:
        remainder = number % 2
        binary_digits = str(remainder) + binary_digits
        number = number // 2
    return binary_digits


print("decimal_to_binary(10) ->", decimal_to_binary(10))
print("decimal_to_binary(25) ->", decimal_to_binary(25))
