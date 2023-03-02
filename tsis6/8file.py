import os
if os.path.exists("flower.txt"):
    os.remove("flower.txt")
else:
    print("File does not exist <3")