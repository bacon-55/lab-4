from math import tan, pi
n = int(input("Input number of sides: "))
l = int(input("Input the lenght of a side: "))

s = float((n * (l**2))/(4*tan(pi/n)))
print("The are of the polygon is:",round(s,4))