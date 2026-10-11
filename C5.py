# Convert three Star-network resistances into equivalent Delta resistances.
def star_to_delta(resistance_a, resistance_b, resistance_c):
    """Return (R_ab, R_bc, R_ca), rounded to two decimal places."""
    if resistance_a <= 0 or resistance_b <= 0 or resistance_c <= 0:
        raise ValueError("All Star resistances must be positive")

    numerator = (resistance_a * resistance_b) + (resistance_b * resistance_c) + (resistance_c * resistance_a)
    resistance_ab = numerator / resistance_c
    resistance_bc = numerator / resistance_a
    resistance_ca = numerator / resistance_b
    return round(resistance_ab, 2), round(resistance_bc, 2), round(resistance_ca, 2)


print(f"star_to_delta(10, 20, 30) -> {star_to_delta(10, 20, 30)}")
