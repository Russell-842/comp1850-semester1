# Week 1.3, Session 2: Word Counter

# We want to read in a text file, and calculate how many words are in it. 
# You can use any of the .txt files to test this - or even make your own.

# open and read the file
from pathlib import Path

filename = input("Enter filename : ")

try:
    file_path = Path(filename)
    if not file_path.is_absolute() and not file_path.exists():
        file_path = Path(__file__).resolve().parent / file_path

    with file_path.open("r") as infile:
        content = infile.read()
    words = content.split()
    print(len(words))
    print(words)
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# calculate the number of words
# hint: you could use .split() to break up by spaces
# hint: watch out for empty lines that might give you empty strings

# display the wordcount

# Here are the word counts you should get:
# story.txt - 290
# story2.txt - 326
# glasses.txt - 210
# ENTER for filename e.g week1.3/session2/task2/1_word_counter/glasses.txt