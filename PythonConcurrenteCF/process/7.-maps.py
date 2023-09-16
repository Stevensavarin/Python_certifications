import time
import logging
from multiprocessing import Pool

logging.basicConfig(level=logging.DEBUG, format="%(message)s")

def is_even(number):
    time.sleep(1)
    return number % 2 == 0


def show_results(results):
    logging.info(f"El resultado es: {results}")


if __name__ == "__main__":
    with Pool(processes=2) as executor:
        numbers = [ number for number in range(1, 11) ]

        map_result = executor.map_async(is_even, numbers, callback=show_results)

        logging.info("Vamos a esperar a que los resultados esten listos")

        map_result.wait()