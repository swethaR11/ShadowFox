#Create a list of your friends' names. The list should have at least 5 names. Create a list of tuples.
# Step 1: List of friends' names
friends = ["thanu", "sandhiya", "madhu", "punitha", "monica"]

# Step 2: Create list of tuples (name, length of name)
name_lengths = [(name, len(name)) for name in friends]

# Print the result
print("List of friends:", friends)
print("List of (name, length) tuples:", name_lengths)
