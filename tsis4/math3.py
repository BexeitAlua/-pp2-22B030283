from math import tan, pi
n = int(input("Input number of sides: "))
b = float(input("Input the length of a side: "))
S = n * (b ** 2) / (4 * tan(pi / n))
print("The area of the polygon is: ",int(S))