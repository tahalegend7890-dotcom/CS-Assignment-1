# Count resistor measurements in 1%, 5%, and reject tolerance bins until 0.
one_percent_count = 0
five_percent_count = 0
reject_count = 0

while True:
    measured_resistance = float(input("Enter measured resistance (0 to stop): "))
    if measured_resistance == 0:
        break

    if 99.0 <= measured_resistance <= 101.0:
        one_percent_count += 1
    elif 95.0 <= measured_resistance <= 105.0:
        five_percent_count += 1
    else:
        reject_count += 1

print(f"1% tolerance: {one_percent_count}")
print(f"5% tolerance: {five_percent_count}")
print(f"Reject: {reject_count}")
