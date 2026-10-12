# Calculate current using Ohm's law and report whether the fuse will blow.
voltage = float(input("Enter voltage (V): "))
resistance = float(input("Enter resistance (ohm): "))

if resistance <= 0:
    print("Invalid resistance")
else:
    current = voltage / resistance
    print("Current =", current, "A")
    if current > 2:
        print("Fuse will blow")
    else:
        print("Circuit is safe")
