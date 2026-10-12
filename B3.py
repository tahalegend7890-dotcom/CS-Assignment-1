# Find sensor reading count, extremes, and average using one loop.
readings = (3.3, 3.1, 3.4, 2.9, 3.6, 3.0, 3.2)
above_threshold = 0
highest = readings[0]
lowest = readings[0]
total = 0.0
reading_count = 0

for reading in readings:
    if reading > 3.2:
        above_threshold += 1
    if reading > highest:
        highest = reading
    if reading < lowest:
        lowest = reading
    total += reading
    reading_count += 1

average = total / reading_count
print("Readings above 3.2 V:", above_threshold)
print("Highest:", round(highest, 1), "V")
print("Lowest:", round(lowest, 1), "V")
print("Average:", round(average, 2), "V")
