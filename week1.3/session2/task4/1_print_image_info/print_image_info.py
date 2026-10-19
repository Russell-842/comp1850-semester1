# Week 1.3, Session 2: Print PGM image info
from pathlib import Path

# Open a pgm image file
# You can use the relative path ../images/filename
# You could handle file errors with try/except.
filename = input("Enter PGM file path (e.g. ../images/with_comment.pgm): ")
image_path = Path(filename)
if not image_path.is_absolute() and not image_path.exists():
	image_path = Path(__file__).resolve().parent / image_path

# Read the file content
try:
	header_values = []
	with image_path.open("r") as image_file:
		for line in image_file:
			line = line.split("#", 1)[0]
			header_values.extend(line.split())
			if len(header_values) >= 4:
				break

	if len(header_values) < 4 or header_values[0] != "P2":
		raise ValueError("The file does not have a valid plain-text PGM header.")

	width = int(header_values[1])
	height = int(header_values[2])
	max_gray_value = int(header_values[3])

	# Print dimensions and max gray value on separate lines.
	print(f"Dimensions: {width} x {height} pixels")
	print(f"Max Gray Value: {max_gray_value}")
except FileNotFoundError:
	print(f"Error: The file '{filename}' was not found.")
except ValueError as error:
	print(f"Error: {error}")