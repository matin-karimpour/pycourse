import math

def str_list_to_float(p):
    return float(p[0]),float(p[1])

def Distance_2D(p1,p2):
    result = math.sqrt((p1[0]- p2[0])**2 + (p1[1] - p2[1])**2)
    return result

first_point = input("insert first point: ")
second_point = input("insert second point: ")

first_point  = str_list_to_float(first_point.split(" "))
second_point = str_list_to_float(second_point.split(" "))

distance = Distance_2D(first_point,second_point)
print(f"Ditance {first_point} and {second_point} is {distance}")