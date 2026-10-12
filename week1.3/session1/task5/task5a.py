# Week 1.3, Session 1: Task 5a

course = "computer science"

for ch in course:
	print(ch)

# Create a list data structure of the characters from the course string
chars = []

for ch in course : 
	chars.append(ch)

print(chars)

# Sort the list into alphabetical order - OPTION 1 :
chars = []

for ch in course : 
	chars.append(ch)

print(sorted(chars))

# Sort the list into alphabetical order - OPTION 2 :
chars = []

for ch in course : 
	chars.append(ch)

chars.sort()
print(chars)

# 'chars' = random list name