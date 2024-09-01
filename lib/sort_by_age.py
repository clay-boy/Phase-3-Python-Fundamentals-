def sort_by_age(people):
    return sorted(people, key=lambda person: person[1])
people = [
    ('Alice', 30),
    ('Bob',25),
    ('Charlie',35),
    ('Diana',22)
]

# Sorting the list by age
sorted_people = sort_by_age(people)

# Print the sorted list
print(sorted_people)
