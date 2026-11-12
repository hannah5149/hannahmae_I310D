import math

def calculate_volume_of_sphere(radius):
 volume = 4 / 3 * math.pi * radius**3

 return volume

print("Volume of sphere, where radius = 30:", calculate_volume_of_sphere(30))
print("Volume of sphere, where radius = 40:", calculate_volume_of_sphere(40))