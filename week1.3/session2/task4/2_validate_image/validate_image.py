# Week 1.3, Session 2: Validate image
from pathlib import Path

filename = input("Enter PGM file path (e.g. ../images/feep.pgm): ")
image_path = Path(filename)
if not image_path.is_absolute() and not image_path.exists():
	image_path = Path(__file__).resolve().parent / image_path

try:
	with image_path.open("r") as image_file:
		rows = [line.split("#", 1)[0].split() for line in image_file]

	header = []
	pixel_rows = []
	for row in rows:
		if not row:
			continue
		if len(header) < 4:
			header_count = 4 - len(header)
			header.extend(row[:header_count])
			row = row[header_count:]
		if row:
			pixel_rows.append([int(pixel) for pixel in row])

	if len(header) < 4 or header[0] != "P2":
		raise ValueError("The file does not have a valid plain-text PGM header.")

	width = int(header[1])
	height = int(header[2])
	max_gray_value = int(header[3])

	if any(len(row) != width for row in pixel_rows):
		print("Invalid width")
	elif len(pixel_rows) != height:
		print("Invalid height")
	elif any(
		pixel < 0 or pixel > max_gray_value
		for row in pixel_rows
		for pixel in row
	):
		print("Invalid pixel values")
	else:
		print("Valid image")
except FileNotFoundError:
	print(f"Error: The file '{filename}' was not found.")
except ValueError as error:
	print(f"Error: {error}")