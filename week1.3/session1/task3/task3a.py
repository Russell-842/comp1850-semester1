# Week 1.3, Session 1: Task 3a

i = 0

while i < 20:
    i = i + 1
    if i % 3 == 0 :
        continue
    print(i)

while i < 20 : 
    i =  i + 1
    if i % 3 != 0 :
        print(i)

# Add logic using continue so that multiples of 3 are not printed out
# Hint: we discused operators such as % and // in recent weeks

# Hint 2: there are several ways to do this - using truthy/falsey values is the least code
# BUT, more than 1 way to write this loop so don't need continue e.g != (meaning 'not equal to')