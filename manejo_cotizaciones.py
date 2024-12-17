'''
Hay servicio que recibe datos de cotización de empresas desde dos fuentes diferentes, A y B.
Formato:
{"name": "BMA", "buy": 105.22, "sell": 105.59, "timestamp": 1734367423775,
"source": "A"}
{"name": "BMA", "buy": 105.22, "sell": 105.59, "timestamp": 1734367423776,
"source": "B"}

Objetico:
Script que procese en loop infito y haga las siguientes 3 acciones:
1. Almacenar los datos recibidos de cada empresa para cada fuente.
2. Imprimir el último precio (buy y sell) recibido de cada empresa y su fuente.
3. Añade validaciones y logs donde creas necesario.
'''

'''

price_companies_A {
    "BMA": [(buy, sell, timestam), (buy, sell, timestam)], // De esta manera me guardo todos los valores historicos
    "YPF": [(buy, sell, timestamp)],
    ...
}

price_companies_B {
    "BMA": [(buy, sell, timestam), (buy, sell, timestam), (buy, sell, timestam)],
    "YPF": [(buy, sell, timestamp), (buy, sell, timestam)],
    ...
}
'''

import random
import time
import logging

# Configuración del logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# Genera data aleatoriamente en el formato pedido
def generate_input():
    companies = ["BMA", "GGAL", "YPF"]
    sources = ["A", "B"]
    
    data = {
        "name": random.choice(companies),
        "buy": round(random.uniform(10, 200), 2),
        "sell": round(random.uniform(10, 200), 2),
        "timestamp": int(time.time() * 1000),
        "source": random.choice(sources)
    }

    return data
    

def loop():
    data_flows = True
    price_companies_A = dict()
    price_companies_B = dict()
    companies = list()

    while data_flows:
        data = generate_input()
        logger.info(f'{data}')
        data_to_save = (data["buy"], data["sell"], data["timestamp"])
        
        if data["name"] not in companies:
            companies.append(data["name"])
        
        if data["source"] == "A":
            if data["name"] not in price_companies_A:
                price_companies_A[data["name"]] = [data_to_save]
            else: 
                price_companies_A[data["name"]].append(data_to_save)

        elif data["source"] == "B":
            if data["name"] not in price_companies_B:
                price_companies_B[data["name"]] = [data_to_save]
            else: 
                price_companies_B[data["name"]].append(data_to_save)
        else:
            logger.error(f"Unkoun source")


        # Imprimo los ultimos precios de las acciones de cada compania para cada fuente
        print("\n\n")
        logger.info(f"Last price of all registered companies: ")
        print("\n")
        for company in companies:
            if company in price_companies_A:
                last_data_A = price_companies_A[company][-1]
                logger.info(f"Last price of {company} from source A: Buy: {last_data_A[0]}, Sell: {last_data_A[1]}")
            if company in price_companies_B:
                last_data_B = price_companies_B[company][-1]
                logger.info(f"Last price of {company} from source B: Buy: {last_data_B[0]}, Sell: {last_data_B[1]}")

            print("\n")

        time.sleep(5)


def main():
    loop()


main()