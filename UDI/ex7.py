import math

op_side = 20

angle = math.radians(22)

adj_side = math.ceil(op_side / math.tan(angle))

print("La longitud de la sombra es: ", adj_side, "m")