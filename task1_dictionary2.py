#Create two dictionaries, one for your expenses and one for your partner's expenses. Each dictionary should contain at least 5 expense categories and their corresponding amounts.
# Step 1: Define expense dictionaries
your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

# Step 2: Calculate total expenses
your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

print("Your total expenses:", your_total)
print("Partner's total expenses:", partner_total)

# Step 3: Determine who spent more
if your_total > partner_total:
    print("You spent more overall.")
elif your_total < partner_total:
    print("Your partner spent more overall.")
else:
    print("Both spent the same amount.")

# Step 4: Find category with maximum difference
max_diff = 0
diff_category = ""

for category in your_expenses:
    diff = abs(your_expenses[category] - partner_expenses[category])
    if diff > max_diff:
        max_diff = diff
        diff_category = category

print(f"The biggest spending difference is in '{diff_category}' with a difference of {max_diff} units.")
