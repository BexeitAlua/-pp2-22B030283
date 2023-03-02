import os
print("Existence:",os.access("input.txt",os.F_OK))
print("Readability:",os.access("input.txt",os.R_OK))
print("Writability:",os.access("input.txt",os.W_OK))
print("Executability",os.access("input.txt",os.X_OK))