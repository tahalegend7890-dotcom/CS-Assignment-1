# Calculate the equivalent resistance of resistors connected in parallel.
def parallel_resistance(resistors):
    """Return the equivalent resistance for a list of positive resistors."""
    reciprocal_total = 0.0
    for resistance in resistors:
        if resistance <= 0:
            raise ValueError("Resistances must be positive")
        reciprocal_total += 1 / resistance
    if reciprocal_total == 0:
        raise ValueError("At least one resistor is required")
    return 1 / reciprocal_total


print(f"parallel_resistance([10, 10]) -> {parallel_resistance([10, 10]):.1f}")
print(f"parallel_resistance([100, 200, 300]) -> {parallel_resistance([100, 200, 300]):.2f}")
