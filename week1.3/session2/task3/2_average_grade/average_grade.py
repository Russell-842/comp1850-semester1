# Week 1.3, Session 2: Calculate Average Grade and Write to a File

import csv
from pathlib import Path

task_directory = Path(__file__).resolve().parent

# Open 'student_data.csv' to read each student's grades
# hint: skip the header row with data[1:]
with (task_directory / "student_data.csv").open(newline="") as infile:
	data = list(csv.reader(infile))

# Read each student's grades and calculate their average grade
# hint: CSV data comes as strings, convert grade columns to int() for maths
# hint: student_data.csv has columns: ID, Name, Mathematics, Science, History
# hint: average = (maths + science + history) / 3
# Open a file called 'report.txt'
# Write each student's name and their average grade to the report
# hint: use 'w' mode to create a fresh report each time
# hint: format averages nicely, maybe to 2 decimal places with :.2f
with (task_directory / "report.txt").open("w") as report:
	for row in data[1:]:
		name = row[1]
		maths = int(row[2])
		science = int(row[3])
		history = int(row[4])
		average = (maths + science + history) / 3
		report.write(f"{name}: {average:.2f}\n")


# Open a file called 'report.txt'
# Write each student's name and their average grade to the report
# hint: use 'w' mode to create a fresh report each time
# hint: format averages nicely, maybe to 2 decimal places with :.2f
