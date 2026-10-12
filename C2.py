# Calculate the equivalent resistance of resistors connected in parallel.
def parallel_resistance(resistors):
    # Add the reciprocal of every resistor, then invert the total.
    reciprocal_total = 0.0
    for resistance in resistors:
        reciprocal_total += 1 / resistance
    equivalent_resistance = 1 / reciprocal_total
    return round(equivalent_resistance, 2)


print("parallel_resistance([10, 10]) ->", parallel_resistance([10, 10]))
print("parallel_resistance([100, 200, 300]) ->", parallel_resistance([100, 200, 300]))
