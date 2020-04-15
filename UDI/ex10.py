import datetime

usrDay = int(input("\nIngrese su dia de nacimiento: "))
usrMonth = int(input("Ingrese su mes de nacimiento: "))
usrYear = int(input("Ingrese su año de nacimiento: "))

usrBday = datetime.datetime(usrYear, usrMonth, usrDay)
today = datetime.date.today()

_months = (usrBday.year - today.year) * 12 + (usrBday.month - today.month)

print("\nHan pasado ", abs(_months), " meses desde su fecha de nacimiento\n")