from services.change_calculation import has_enough_change
from json import load as json_load

if __name__ == "__main__":
    with open("input.json") as file:
        input = json_load(file)

    response = has_enough_change(input['COLA_PAGO'])
    print(f"Vania {response} puede vender boletos y dar cambio")
