"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Russell Gonzales
"""
# Dictionary defining traffic light passing through a repeating set of states, with a fixed duration
states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input())  # read an integer number of steps (>0)

state = "red" 

print(f"Time {systime:003} State {state}")

time_in_state = 1

while systime < maxtime :
    if time_in_state >= states[state] :
        if state == "red" :
            state = "red_amber"
        elif state == "red_amber" :
            state = "green"
        elif state == "green" :
            state = "amber"
        else :
            state = "red"

        time_in_state = 0
    systime += 1
    time_in_state += 1

    print(f"Time {systime:003} State {state}")

# Simulate the traffic light system up to time=maxtime in 1-second steps

# At the end of each step you should output the time and state using the statement on line 14