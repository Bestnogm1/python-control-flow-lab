# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equilateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

a = int(input( "Enter a " ))
b = int(input( "Enter b " ))
c = int(input( "Enter c " ))

if a == b and a == c and b == c :
  print( f"{a} {b} {c} is a equilateral" )
if a == b or a == c or c == b :
  print( f"{a} {b} {c} is a isosceles" )
elif a != b and a != c and b != c :
  print( f"{a} {b} & {c} is a scalene " )