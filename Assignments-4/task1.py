import os

if os.path.exists("sample.txt"):
    with open("sample.txt","r") as fh:
        content = fh.read()
        c=1
        for line in content.splitlines():
            print(f"Line {c}: {line}")
            c+=1
else:
    print("Error: The file 'sample.txt' was not found")