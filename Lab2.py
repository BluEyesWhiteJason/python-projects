
width = float(input("Please enter width of room: "))

length = float(input("Please enter length of room: "))

height = float(input("Please enter height of room: "))

area = width * length
perimeter = width * 2 + length * 2
volume = width * length * height

print("The area is {} and the perimiter is {} and the volume is {}".format(area, perimeter, volume))