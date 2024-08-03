# ----Stores the files location to FILE_PATH.----
FILE_PATH = r"10-018 IO Operations - Input\Task file\DOB.txt"

# Outputs file location.
print(FILE_PATH)

# File is opened using UTF-8 encoding.
with open(FILE_PATH, 'r', encoding="UTF-8") as file:
    # All lines in DOB.text is read into DOB_Info
    DOB_INFO = file.readlines()

# ----Processing the Name column----
print("Name:", end='')

# Loop starts in DOB_INFO
for line in DOB_INFO:

    # Words in the line are split into individual words
    parts = line.split()
    # Words 0 to words 2 are joined together
    NAME_SURNAME = " ".join(parts[0:2])
    # Displays combined words of [0:2]
    print(NAME_SURNAME)

# ----Processing the Birthdate column----
print("\nBirthdate:", end='')

# Loop starts in DOB_INFO
for line in DOB_INFO:

    # Words in the line are split into individual words
    parts = line.split()
    # Words from 3 onwards grouped together
    BIRTH_DATE = " ".join(parts[2:])
    # Displays combined words of [2:]
    print(BIRTH_DATE)
