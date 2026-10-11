# Find the smallest and largest of three resistor values using conditions.
resistor_1 = float(input("Enter R1: "))
resistor_2 = float(input("Enter R2: "))
resistor_3 = float(input("Enter R3: "))

if resistor_1 <= resistor_2 and resistor_1 <= resistor_3:
    smallest = resistor_1
elif resistor_2 <= resistor_1 and resistor_2 <= resistor_3:
    smallest = resistor_2
else:
    smallest = resistor_3

if resistor_1 >= resistor_2 and resistor_1 >= resistor_3:
    largest = resistor_1
elif resistor_2 >= resistor_1 and resistor_2 >= resistor_3:
    largest = resistor_2
else:
    largest = resistor_3

print(f"Smallest = {smallest:g} ohm")
print(f"Largest = {largest:g} ohm")
