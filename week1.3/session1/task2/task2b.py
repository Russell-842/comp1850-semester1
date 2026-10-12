# Week 1.3, Session 1: Task 2b

print("This program will repeat everything you type.")
print("To exit the program, type quit")

while True:
    user_input = input("Say something: ")
    if user_input.lower() == "quit" :
        break
    print(f"You said: {user_input}")

# lower() is more user-friendly and allows code to work for uppercase and lowercase 
# As written the program has an infinite loop.
# Add a break statement so that if the user types 'quit' the program exits.