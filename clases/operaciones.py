class Operaciones:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.resultado = 0
        
    def leerNumeros(self):
        while True:
            try:
                self.num1 = int(input("Número 1: "))
                break
            except Exception:
                print("Número inválido")
                continue
        while True:
            try:
                self.num2 = int(input("Número 2: "))
                break
            except Exception:
                print("Número inválido")
                continue    
    
    def sumar(self):
        self.resultado = f"La suma de {self.num1} + {self.num2} es igual a {self.num1 + self.num2}"
        self.mostrarResultado()
    
    def restar(self):
        self.resultado = f"La resta de {self.num1} - {self.num2} es igual a {self.num1 - self.num2}"
        self.mostrarResultado()
    
    def multiplicar(self):
        self.resultado = f"La multiplicación de {self.num1} * {self.num2} es igual a {self.num1 * self.num2}"
        self.mostrarResultado()
    
    def dividir(self):
        try:
            resultado_div = self.num1 / self.num2
            self.resultado = f"La división de {self.num1} / {self.num2} es igual a {resultado_div}"
        except ZeroDivisionError:
            self.resultado = "Error: No se puede dividir entre cero."
        self.mostrarResultado()
    
    def modulo(self):
        try:
            resultado_mod = self.num1 % self.num2
            self.resultado = f"El módulo de {self.num1} % {self.num2} es igual a {resultado_mod}"
        except ZeroDivisionError:
            self.resultado = "Error: No se puede calcular el módulo con divisor cero."
        self.mostrarResultado()
    
    def mostrarResultado(self):
        print(self.resultado)

def menu():
    operaciones = Operaciones()
    while True:
        print("\n¿Qué operación deseas realizar?")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Módulo")
        print("6. Salir")
        opcion = input("Selecciona una opción (1-6): ")
        
        if opcion == "6":
            print("¡Hasta luego!")
            break
        elif opcion in ["1", "2", "3", "4", "5"]:
            operaciones.leerNumeros()
            if opcion == "1":
                operaciones.sumar()
            elif opcion == "2":
                operaciones.restar()
            elif opcion == "3":
                operaciones.multiplicar()
            elif opcion == "4":
                operaciones.dividir()
            elif opcion == "5":
                operaciones.modulo()
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()

