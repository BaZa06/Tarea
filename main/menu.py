import models.classes as c
import dao.functions as f

promedio = f.PromedioDao()

def menu():
    print("""
          1. Agregar
          2. Mostrar
          6. Salir
          Digite una opcion:
          """)
def main():
        while (True):
            menu()
            option = input()
            if option == '1':
                nombre = input("Nombre del alumno:")
                apellido = input("Apelledio del alumno: ")
                carrera = input("Carrera del alumno: ")
                año = int(input("Año del alumno:"))
                promedio = c.Promedio(nombre, apellido, carrera, año)
                promedio.add(promedio)
                
            elif option == '2':
                print("Promedio")
                promedio.show()
            elif option == '6':
                print("Adios")
                False
                
                
                
                break
            else:
                print("Opcion no valida, intente de nuevo")