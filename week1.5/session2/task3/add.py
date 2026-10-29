# Week 1.5, Session 2: Task 3

# Write a program here that creates two Money objects, prints them,
# then adds them together and prints their sum

from money import Money

m1 = Money(1, 99)
print(m1)
m2 = Money(2, 50)
print(m2)
total = m1 + m2
print(f"Total : {total}")
m3 = Money(-5, 10)  # This should raise a ValueError
print(m3)