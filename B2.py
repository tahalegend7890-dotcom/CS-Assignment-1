# Add the resistance values of a series-connected group of resistors.
resistor_count = int(input("How many resistors? "))
total_resistance = 0.0

for resistor_number in range(1, resistor_count + 1):
    resistance = float(input(f"Enter R{resistor_number}: "))
    total_resistance += resistance

print("Total resistance =", total_resistance, "ohm")
