# Week 1.7, Session 2: Task 1 - ValueError

# Run this program and observe what happens

user_profile = {"username": "alice99", "role": "admin"}

# Add .items() as it is a dictionary
for key, value in user_profile.items() :
	print(f"{key} : {value}")

# ValueError : too many values to unpack (expected 2)