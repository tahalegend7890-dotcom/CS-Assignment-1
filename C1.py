# Calculate current and resistor power with reusable functions.
def ohms_current(voltage, resistance):
    """Return current from voltage and resistance."""
    return voltage / resistance


def power_dissipated(current, resistance):
    """Return the power dissipated by a resistor."""
    return current ** 2 * resistance


voltage = 12
resistance = 6
current = ohms_current(voltage, resistance)
power = power_dissipated(current, resistance)
print(f"Current = {current} A")
print(f"Power = {power} W")
