class ClimaDiario:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperatura(self, temperatura):
        self.temperaturas.append(temperatura)

    def calcular_promedio(self):
        if not self.temperaturas:
            return 0
        return sum(self.temperaturas) / len(self.temperaturas)


def main():
    clima = ClimaDiario()
    print("Cálculo del promedio semanal de temperaturas")

    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        clima.ingresar_temperatura(temp)

    promedio = clima.calcular_promedio()
    print(f"El promedio semanal de temperaturas es: {promedio:.2f} °C")


if __name__ == "__main__":
    main()
