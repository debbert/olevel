# Variable declarations
# input_text : str
# acronym    : str
# index      : int

# Input
input_text = input("Enter the input text: ")

# Process
acronym = ""
index = 0
while index < len(input_text):
    if input_text[index - 1].isspace() or index == 0:
        acronym += input_text[index]
    print("Debug: when index=" + str(index) + ", acronym=" + acronym)
    index += 1
acronym = acronym.upper()

# Output
print(acronym)