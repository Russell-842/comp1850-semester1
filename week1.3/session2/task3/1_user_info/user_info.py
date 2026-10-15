# Week 1.3, Session 2: Write User Information to a File

# Prompt the user for their name, age, and favorite colour.
name = input("Enter your name : ")
age = int(input("Enter your age : "))
favourite_colour = input("Enter your favourite colour : ")

# Open a file called 'user_info.txt' for reading
with open("user_info.txt", "w") as outfile :
    outfile.write("Hello")

# Write each piece of information to the file, each on a new line.


# Hints:
# - Remember to add \n for new lines when writing to files


# Optional: extend this by using a loop to allow multiple people to enter their info in a row
# If you want multiple people to add info without overwriting, consider append mode 'a'
