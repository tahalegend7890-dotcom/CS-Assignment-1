# Print the current through a fixed 10-ohm resistor for voltages 1 to 10 V.
resistance = 10

for voltage in range(1, 11):
    current = voltage / resistance
    print("V =", voltage, "V, I =", round(current, 1), "A")
