# Week 1.5, Session 2: Task 5

# Write a program here to create a Dataset containing data
# from a file named by the user

filename = input("Enter the name of the dataset file : ")

data = []

try:
    with open(filename, "r") as file:
        for line in file:
            for item in line.split():
                try:
                    data.append(float(item))
                except ValueError:
                    pass
except FileNotFoundError:
    print(f"File '{filename}' not found.")
    data = []

# Your program should display dataset size, mean and median,
# followed by the individual values (using a for loop)

# Make sure the file actually contains numbers
if len(data) == 0:
    print("No numeric data found in the file.")
else:
    import statistics

    print("Dataset size:", len(data))
    print("Mean:", statistics.mean(data))
    print("Median:", statistics.median(data))

    print("Values:")
    for value in data:
        print(value)