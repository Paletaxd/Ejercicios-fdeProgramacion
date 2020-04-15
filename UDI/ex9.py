ES_score = float(input("Cual fue su nota en Español?: "))

MATH_score = float(input("Cual fue su nota en Matematicas?: "))

ECON_score = float(input("Cual fue su nota en Economia?: "))

PROG_score = float(input("Cual fue su nota en Programacion?: "))

ENG_score = float(input("Cual fue su nota en Ingles?: "))

avgScore = (ES_score + MATH_score + ECON_score + PROG_score + ENG_score) / 5

print("\nSu promedio de notas es de ", avgScore)