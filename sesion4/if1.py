#Leer nota de un estudiante y determinar si aprueba o reprueba
from colorama import Fore, Back, Style
grade = int(input("Ingrese la nota:"))

if( grade >= 70):
    print(Fore.GREEN + "El estudiante aprueba")
else:
    print(Fore.RED + "Su aprendizaje es inicial, debe mejorar")
print(Style.RESET_ALL)