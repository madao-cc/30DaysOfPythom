#!/usr/bin/env python3

#DAY 1

import math

# Level 1 and 2
print(3 + 4)  # addition(+)
print(3 - 4)  # subtraction(-)
print(3 * 4)  # multiplication(*)
print(3 / 4)  # division(/)
print(3 ** 4)  # exponential(**)
print(3 % 4)  # modulus(%)
print(3 // 4)  # floor division operator(//)

print(type(10))  # Int
print(type(9.8))  # Float
print(type(3.14))  # Float
print(type(4-4j))  # Complex
print(type(['Head', 'Arms', 'Legs']))  # List

# Level 3: Calculate the Euclidian distance between (2, 3) and (10, 8).
x1, y1 = 2, 3
x2, y2 = 10, 8

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Euclidian distance:", distance)