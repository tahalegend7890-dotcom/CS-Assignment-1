# Convert three Star-network resistances into equivalent Delta resistances.
def star_to_delta(resistance_a, resistance_b, resistance_c):
    # Calculate the shared numerator used in all three Delta resistances.
    numerator = (resistance_a * resistance_b) + (resistance_b * resistance_c) + (resistance_c * resistance_a)
    resistance_ab = numerator / resistance_c
    resistance_bc = numerator / resistance_a
    resistance_ca = numerator / resistance_b
    return round(resistance_ab, 2), round(resistance_bc, 2), round(resistance_ca, 2)


print("star_to_delta(10, 20, 30) ->", star_to_delta(10, 20, 30))
