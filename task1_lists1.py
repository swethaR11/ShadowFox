# Step 1: Original list
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("1. Original Justice League members:", justice_league)

# Step 1: Calculate number of members
print("Number of members:", len(justice_league))

# Step 2: Add Batgirl and Nightwing
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("\n2. After adding Batgirl and Nightwing:", justice_league)

# Step 3: Move Wonder Woman to the beginning (leader)
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("\n3. After making Wonder Woman the leader:", justice_league)

# Step 4: Separate Aquaman and Flash by placing Superman in between
# First, remove Superman from current position
justice_league.remove("Superman")

# Find the index of Aquaman and Flash
index_aquaman = justice_league.index("Aquaman")
index_flash = justice_league.index("Flash")

# Place Superman between Aquaman and Flash (assuming Aquaman comes before Flash)
# We insert after Aquaman, so index is index_aquaman + 1
justice_league.insert(index_aquaman + 1, "Superman")
print("\n4. After placing Superman between Aquaman and Flash:", justice_league)

# Step 5: Replace entire list with new team
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("\n5. After replacing with a new team:", justice_league)

# Step 6: Sort alphabetically
justice_league.sort()
print("\n6. After sorting alphabetically:", justice_league)
print("New leader (0th index):", justice_league[0])

