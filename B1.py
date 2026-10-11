# Print the current through a fixed 10-ohm resistor for voltages 1 to 10 V.
resistance = 10

for voltage in range(1, 11):
    current = voltage / resistance
    print(f"V = {voltage} V, I = {current:.1f} A")
