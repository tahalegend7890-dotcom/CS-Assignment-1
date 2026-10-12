# Compare unloaded and loaded output voltages for a voltage divider.
def loaded_divider(source_voltage, resistor_1, resistor_2, load_resistance):
    # First calculate the divider without a load.
    unloaded_voltage = source_voltage * resistor_2 / (resistor_1 + resistor_2)

    # The load and resistor 2 are in parallel.
    parallel_resistance = (resistor_2 * load_resistance) / (resistor_2 + load_resistance)
    loaded_voltage = source_voltage * parallel_resistance / (resistor_1 + parallel_resistance)
    return unloaded_voltage, loaded_voltage


result = loaded_divider(12, 1000, 1000, 500)
print("loaded_divider(12, 1000, 1000, 500) ->", (round(result[0], 1), round(result[1], 1)))
