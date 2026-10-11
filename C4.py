# Compare unloaded and loaded output voltages for a voltage divider.
def loaded_divider(source_voltage, resistor_1, resistor_2, load_resistance):
    """Return (unloaded output voltage, loaded output voltage)."""
    if resistor_1 <= 0 or resistor_2 <= 0 or load_resistance <= 0:
        raise ValueError("All resistance values must be positive")

    unloaded_voltage = source_voltage * resistor_2 / (resistor_1 + resistor_2)
    parallel_resistance = (resistor_2 * load_resistance) / (resistor_2 + load_resistance)
    loaded_voltage = source_voltage * parallel_resistance / (resistor_1 + parallel_resistance)
    return unloaded_voltage, loaded_voltage


result = loaded_divider(12, 1000, 1000, 500)
print(f"loaded_divider(12, 1000, 1000, 500) -> ({result[0]:.1f}, {result[1]:.1f})")
