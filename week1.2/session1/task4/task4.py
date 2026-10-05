# Week 1.2, Session 1: Task 4

fruit = {"apple", "orange", "tomato"}
vegetables = {"leek", "tomato", "potato"}

# What do you think will be printed here?
# prints out "tomato" as it is in both sets of lists

both = fruit.intersection(vegetables)
print(both)

# Why does the following code diplay five items?
# "tomato" is already in both lists, so it prints out the rest of fruit and vegetables

food = fruit.union(vegetables)
print(food)

# Add an item to fruit
fruit.add("banana")
print(fruit)

# Remove an item from vegetables
vegetables.discard("leek")
print(vegetables)

# Find and display symmetric difference of the two sets
both = fruit.symmetric_difference(vegetables)
print(both)