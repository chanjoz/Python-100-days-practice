from math import pi,sqrt
radius = float(input("pls input radius: "))
perimeter = 2*pi*radius
area = radius**2*pi
print("The Circle\'s perimeter is %.2f" % perimeter)
print("The Circle\'s area is %.2f" % area)


"""
f and c degree conversion
"""
F = float(input("pls input fahrenheit: "))
C = (F-32)/1.8
print(f'{F:.1f}Fahren = {C:.1f}Cel')


"""
check if it is a leap year
"""
year = int(input("pls input a year: "))
is_leap = year % 4 == 0 and year % 100 != 0 or\
    year % 400 == 0
print(is_leap)


"""
Imperial metric conversion
"""
length = float(input("pls input length number: "))
l_unit = input("pls input length's unit: ")
if l_unit == 'inch':
    metric_len = length * 2.54
    print("the Imperial length %.2f inch equal to Metric length %.2f cm" %
          (length, metric_len))
elif l_unit == 'cm':
    imperial_len = length / 2.54
    print("the metric length %.2f cm equal to Imperial length %.2f inch" %
          (length, imperial_len))
else:
    print("length unit must be inch or cm")

"""
Check if a b c can form a triangle
"""
a = float(input("pls input 1st side len: "))
b = float(input("pls input 2nd side len: "))
c = float(input("pls input 3rd side len: "))
if a + b > c and a + c > b and b + c > a:
    p = (a + b + c) / 2
    area = sqrt(p * (p - a) * (p - b) * (p - c))
    print("%.2f, %.2f and %.2f can form a triangle with area equal to:"
          "%.2f" % (a, b, c, area))
else:
    print("%f, %f and %f can't form a triangle" % (a, b, c))
