# Create and demonstrate a frozen set

my_frozen_set = frozenset([10, 20, 30, 40])

print("Frozen set:", my_frozen_set)
print("Length:", len(my_frozen_set))
print("Is 20 present?", 20 in my_frozen_set)

# Frozen sets are immutable and do not support add() or remove().
