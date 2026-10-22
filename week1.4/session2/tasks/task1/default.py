# Week 4, Session 2: Task 1

def greeting(name='Russell'):
    # Your task is change the default name to your name and observe the output
    print(f'Good morning {name}!')


# Check if correct output is produced
greeting()

# write a second test by passing a name to the function
def greet(name, greeting="Hello", punctuation = "!") :
    return f"{greeting}, {name}{punctuation}"
print(greet("Russell")) # Hello, Russell!