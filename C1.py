# Calculate current and resistor power with reusable functions.
def ohms_current(voltage, resistance):
    # Return the current using Ohm's law.
    return voltage / resistance


def power_dissipated(current, resistance):
    # Return power using P = I squared times R.
    return current ** 2 * resistance


voltage = 12
resistance = 6
current = ohms_current(voltage, resistance)
power = power_dissipated(current, resistance)
print("Current =", current, "A")
print("Power =", power, "W")
