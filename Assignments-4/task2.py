text = input("Enter text to write to the file: ")

with open("output.txt", "w") as f:
    f.write(text + "\n")

print("Data successfully written to output.txt.\n")

extra_text = input("Enter additional text to append: ")

with open("output.txt", "a") as f:
    f.write(extra_text + "\n")

print("Data successfully appended.\n")

print("Final content of output.txt:")

with open("output.txt", "r") as f:
    print(f.read())
