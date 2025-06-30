#Python program to calculate the area of a circular pond and the total water it can hold, using the given values
# Given values
radius = 84
pi = 3.14
water_per_sq_meter = 1.4

# Calculate area of the pond
pond_area = pi * (radius ** 2)

# Calculate total water in liters
total_water = pond_area * water_per_sq_meter

# Print total water without any decimal point (as integer)
print("Total water in the pond (in liters):", int(total_water))

