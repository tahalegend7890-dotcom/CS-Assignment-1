# Determine the direction of current from its signed value.
current = float(input("Enter current (A): "))

if current > 0:
    print("Current flows from A to B")
elif current < 0:
    print("Current flows from B to A")
else:
    print("No current flows")
