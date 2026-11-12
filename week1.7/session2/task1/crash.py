# Week 1.7, Session 2: Task 1 - IndexError

# Run this program and observe what happens

def assign_values(x):
    for i in range(100):
        x[i] = (i + 1) * (i + 1);

if __name__ == "__main__":
    # Changing 10 in data to 100, to be within range (matching 100 in code)
    data = [0] * 100
    assign_values(data)
    print("Done!")

# IndexError : list assignment index out of range