# 1. Write to a file
file = open("allwin.txt", "w")
file.write("Hello, this is Day 7 Python practice.\n")
file.write("Learning file handling in Python.\n")
file.write("I am improving day by day.\n")
file.close()

print("Data written successfully.")


# 2. Read from the file
file = open("allwin.txt", "r")
content = file.read()
print("\nFile Content:")
print(content)
file.close()


# 3. Append new data
file = open("allwin.txt", "a")
file.write("This line is added using append mode.\n")
file.close()

print("New data appended successfully.")


# 4. Count total lines
file = open("allwin.txt", "r")
lines = file.readlines()
print("Total lines in file:", len(lines))
file.close()
